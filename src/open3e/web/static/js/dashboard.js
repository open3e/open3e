/* open3e web UI — dashboard with live uPlot charts */

var MAX_POINTS = 1800; // 30 minutes at 1 sample/second

// Map of "ecu_did" -> { chart: uPlot|null, times: [], values: [], observer: ResizeObserver|null }
var chartState = {};

var wsApi = null;

document.addEventListener("DOMContentLoaded", function () {
    wsApi = openWebSocket();
    wsApi.onDidValue = handleDidValue;
    wsApi.onEngineState = handleEngineState;

    // Subscribe to all DIDs — handle both "already open" and "not yet open"
    if (wsApi.socket.readyState === WebSocket.OPEN) {
        wsApi.subscribe("*");
    } else {
        wsApi.socket.addEventListener("open", function () {
            wsApi.subscribe("*");
        });
    }

    // Fallback: poll last known values every 5 seconds via REST
    // This ensures dashboard shows data even if WebSocket has issues
    function pollValues() {
        fetch("/api/engine/values").then(function(r) { return r.json(); }).then(function(values) {
            for (var key in values) {
                var parts = key.split(":");
                if (parts.length === 2) {
                    var msg = {ecu: parseInt(parts[0]), did: parseInt(parts[1]), value: values[key], ts: Math.floor(Date.now()/1000)};
                    handleDidValue(msg);
                }
            }
        }).catch(function() {});
    }
    setInterval(pollValues, 5000);
    setTimeout(pollValues, 1000);  // first poll after 1 second
});

function handleDidValue(msg) {
    var key = msg.ecu + "_" + msg.did;
    var cardId = "card-" + key;
    var card = document.getElementById(cardId);
    if (!card) { return; }

    var valueEl = card.querySelector(".card-value");
    var tsEl = card.querySelector(".card-ts");

    if (valueEl) {
        valueEl.textContent = formatValue(msg.value);
    }
    if (tsEl) {
        var d = new Date(msg.ts * 1000);
        tsEl.textContent = d.toLocaleTimeString();
    }

    // Feed chart data
    var state = chartState[key];
    if (state) {
        var numeric = extractNumeric(msg.value);
        if (numeric !== null) {
            state.times.push(msg.ts);
            state.values.push(numeric);
            // Trim to rolling window
            if (state.times.length > MAX_POINTS) {
                state.times.shift();
                state.values.shift();
            }
            if (state.chart) {
                state.chart.setData([state.times.slice(), state.values.slice()]);
            }
        }
    }
}

function handleEngineState(msg) {
    var badge = document.getElementById("engine-state-badge");
    if (!badge) { return; }
    var state = msg.state || "unknown";
    badge.textContent = state;
    badge.className = "badge";
    if (state === "polling") {
        badge.classList.add("bg-success");
    } else if (state === "connecting" || state === "paused") {
        badge.classList.add("bg-warning", "text-dark");
    } else {
        badge.classList.add("bg-secondary");
    }
}

function formatValue(value) {
    if (value === null || value === undefined) { return "--"; }
    if (typeof value !== "object") { return String(value); }
    // ComplexType: prefer Actual
    if (value.Actual !== undefined) { return String(value.Actual); }
    // First numeric field
    var keys = Object.keys(value);
    for (var i = 0; i < keys.length; i++) {
        if (typeof value[keys[i]] === "number") {
            return String(value[keys[i]]);
        }
    }
    return JSON.stringify(value);
}

function extractNumeric(value) {
    if (value === null || value === undefined) { return null; }
    if (typeof value === "number") { return value; }
    if (typeof value !== "object") {
        var f = parseFloat(value);
        return isNaN(f) ? null : f;
    }
    if (typeof value.Actual === "number") { return value.Actual; }
    var keys = Object.keys(value);
    for (var i = 0; i < keys.length; i++) {
        if (typeof value[keys[i]] === "number") {
            return value[keys[i]];
        }
    }
    return null;
}

function toggleChart(ecu, did, name) {
    var key = ecu + "_" + did;
    var containerId = "chart-" + key;
    var container = document.getElementById(containerId);
    if (!container) { return; }

    var state = chartState[key];

    if (state && state.chart) {
        // Destroy chart
        if (state.observer) {
            state.observer.disconnect();
            state.observer = null;
        }
        state.chart.destroy();
        state.chart = null;
        container.style.display = "none";
        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }
        return;
    }

    // Create chart state if not present
    if (!state) {
        state = { chart: null, times: [], values: [], observer: null };
        chartState[key] = state;
    }

    container.style.display = "block";

    var opts = {
        title: name,
        width: container.offsetWidth || 400,
        height: 200,
        series: [
            {},
            {
                label: name,
                stroke: "#4dabf7",
                width: 2,
            },
        ],
        axes: [
            {
                stroke: "#adb5bd",
                grid: { stroke: "rgba(255,255,255,0.1)" },
                ticks: { stroke: "rgba(255,255,255,0.1)" },
            },
            {
                stroke: "#adb5bd",
                grid: { stroke: "rgba(255,255,255,0.1)" },
                ticks: { stroke: "rgba(255,255,255,0.1)" },
            },
        ],
        scales: { x: { time: true } },
    };

    var data = [state.times.slice(), state.values.slice()];
    if (data[0].length === 0) {
        data = [[0], [null]];
    }

    state.chart = new uPlot(opts, data, container);

    // Auto-resize
    state.observer = new ResizeObserver(function (entries) {
        if (!state.chart) { return; }
        var entry = entries[0];
        var width = entry.contentRect.width;
        if (width > 0) {
            state.chart.setSize({ width: width, height: 200 });
        }
    });
    state.observer.observe(container);
}
