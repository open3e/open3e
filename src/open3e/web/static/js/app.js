/* open3e web UI — shared JavaScript utilities */

/**
 * Show a Bootstrap toast notification.
 * @param {string} message - Text to display
 * @param {string} type - "success", "danger", "warning", "info"
 */
function showToast(message, type = "info") {
    const container = document.getElementById("toast-container");
    if (!container) return;

    const id = "toast-" + Date.now();
    const html = `
        <div id="${id}" class="toast align-items-center text-bg-${type} border-0" role="alert">
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto"
                        data-bs-dismiss="toast"></button>
            </div>
        </div>`;
    container.insertAdjacentHTML("beforeend", html);

    const el = document.getElementById(id);
    const toast = new bootstrap.Toast(el, { delay: 4000 });
    toast.show();
    el.addEventListener("hidden.bs.toast", () => el.remove());
}

/**
 * Send a PATCH/POST request with JSON body and show result toast.
 * @param {string} url
 * @param {string} method - "PATCH", "POST", "DELETE"
 * @param {object} body
 * @returns {Promise<object>} parsed JSON response
 */
async function apiCall(url, method, body = null) {
    const opts = {
        method: method,
        headers: { "Content-Type": "application/json" },
    };
    if (body !== null) {
        opts.body = JSON.stringify(body);
    }
    const resp = await fetch(url, opts);
    const data = await resp.json();
    if (!resp.ok) {
        showToast(data.detail || "Request failed", "danger");
        throw new Error(data.detail || resp.statusText);
    }
    return data;
}

/**
 * Open a WebSocket connection to the server and return a control object.
 * @returns {object} API object with subscribe, write, close methods and callback properties
 */
function openWebSocket() {
    var protocol = window.location.protocol === "https:" ? "wss://" : "ws://";
    var url = protocol + window.location.host + "/ws";

    var api = {
        socket: null,
        _closed: false,
        onDidValue: null,
        onEngineState: null,
        onCanStatus: null,
        onMqttStatus: null,
        onDepictProgress: null,
        onDepictComplete: null,
        onWriteResult: null,
        onError: null,
    };

    function connect() {
        var ws = new WebSocket(url);
        api.socket = ws;

        ws.onmessage = function (event) {
            var msg;
            try {
                msg = JSON.parse(event.data);
            } catch (e) {
                return;
            }
            switch (msg.type) {
                case "did_value":
                    if (api.onDidValue) { api.onDidValue(msg); }
                    break;
                case "engine_state":
                    if (api.onEngineState) { api.onEngineState(msg); }
                    break;
                case "can_status":
                    if (api.onCanStatus) { api.onCanStatus(msg); }
                    updateCanIndicator(msg);
                    break;
                case "mqtt_status":
                    if (api.onMqttStatus) { api.onMqttStatus(msg); }
                    updateMqttIndicator(msg.connected);
                    break;
                case "depict_progress":
                    if (api.onDepictProgress) { api.onDepictProgress(msg); }
                    break;
                case "depict_complete":
                    if (api.onDepictComplete) { api.onDepictComplete(msg); }
                    break;
                case "write_result":
                    if (api.onWriteResult) { api.onWriteResult(msg); }
                    break;
                case "error":
                    if (api.onError) { api.onError(msg); }
                    break;
                default:
                    break;
            }
        };

        ws.onclose = function () {
            if (!api._closed) {
                setTimeout(connect, 3000);
            }
        };
    }

    api.subscribe = function (dids) {
        if (api.socket && api.socket.readyState === WebSocket.OPEN) {
            api.socket.send(JSON.stringify({ type: "subscribe", dids: dids }));
        }
    };

    api.write = function (ecu, did, value, sub) {
        if (api.socket && api.socket.readyState === WebSocket.OPEN) {
            api.socket.send(JSON.stringify({
                type: "write",
                ecu: ecu,
                did: did,
                value: value,
                sub: sub,
            }));
        }
    };

    api.close = function () {
        api._closed = true;
        if (api.socket) {
            api.socket.close();
        }
    };

    connect();
    return api;
}

/**
 * Update sidebar status indicator dots based on an engine state message.
 * @param {object} msg - Message with a "state" property
 */
var _lastEngineState = null;
var _lastMqttState = null;
var _lastCanState = null;

function updateStatusIndicators(msg) {
    var state = msg.state;
    if (state === _lastEngineState) { return; }
    _lastEngineState = state;

    var engineDot = document.getElementById("status-engine");
    var engineText = document.getElementById("status-engine-text");
    var canDot = document.getElementById("status-can");
    var canText = document.getElementById("status-can-text");

    if (!engineDot || !engineText) { return; }

    switch (state) {
        case "polling":
            engineDot.className = "status-dot green";
            engineText.textContent = "running";
            engineText.className = "text-success";
            if (canDot) { canDot.className = "status-dot green"; }
            if (canText) { canText.textContent = "connected"; canText.className = "text-success"; }
            break;
        case "connecting":
            engineDot.className = "status-dot amber";
            engineText.textContent = "connecting";
            engineText.className = "text-warning";
            break;
        case "paused":
            engineDot.className = "status-dot amber";
            engineText.textContent = "scanning";
            engineText.className = "text-warning";
            break;
        case "idle":
            engineDot.className = "status-dot gray";
            engineText.textContent = "not running";
            engineText.className = "text-danger";
            if (canDot) { canDot.className = "status-dot gray"; }
            if (canText) { canText.textContent = "not connected"; canText.className = "text-danger"; }
            break;
        default:
            engineDot.className = "status-dot gray";
            engineText.textContent = state || "unknown";
            engineText.className = "text-muted";
            break;
    }
}

function updateCanIndicator(msg) {
    var state = msg.state || "";
    if (state === _lastCanState) { return; }
    _lastCanState = state;
    var dot = document.getElementById("status-can");
    var text = document.getElementById("status-can-text");
    if (!dot || !text) { return; }
    if (state === "up" || state === "connected") {
        dot.className = "status-dot green";
        text.textContent = "connected";
        text.className = "text-success";
    } else if (state === "scanning") {
        dot.className = "status-dot amber";
        text.textContent = "scanning";
        text.className = "text-warning";
    } else {
        dot.className = "status-dot gray";
        text.textContent = state || "not connected";
        text.className = "text-danger";
    }
}

function updateMqttIndicator(connected) {
    if (connected === _lastMqttState) { return; }
    _lastMqttState = connected;
    var dot = document.getElementById("status-mqtt");
    var text = document.getElementById("status-mqtt-text");
    if (!dot || !text) { return; }
    if (connected) {
        dot.className = "status-dot green";
        text.textContent = "connected";
        text.className = "text-success";
    } else {
        dot.className = "status-dot gray";
        text.textContent = "not connected";
        text.className = "text-danger";
    }
}
