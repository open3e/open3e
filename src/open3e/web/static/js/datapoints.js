/* open3e web UI — datapoints browser */

var wsApi = null;

document.addEventListener("DOMContentLoaded", function () {
    wsApi = openWebSocket();
    wsApi.onDidValue = handleDidValue;

    wsApi.socket.addEventListener("open", function () {
        wsApi.subscribe("*");
    });
});

function formatValue(value) {
    if (value === null || value === undefined) { return "--"; }
    if (typeof value !== "object") { return String(value); }
    // For ComplexType with Actual — show just the Actual value prominently
    if (value.Actual !== undefined) {
        return String(value.Actual);
    }
    // Show all sub-fields compactly: "String1:0 String2:2065 String3:3632"
    var parts = [];
    var keys = Object.keys(value);
    for (var i = 0; i < keys.length; i++) {
        var k = keys[i];
        var v = value[k];
        if (v === null || v === undefined) continue;
        if (typeof v === "object") {
            // Nested dict — show Text if available, else compact JSON
            if (v.Text !== undefined) { parts.push(k + ":" + v.Text); }
            else if (v.ID !== undefined) { parts.push(k + ":" + v.ID); }
            else { parts.push(k + ":" + JSON.stringify(v)); }
            continue;
        }
        parts.push(k + ":" + v);
    }
    return parts.join(" | ");
}

function handleDidValue(msg) {
    var cellId = "val-" + msg.ecu + "_" + msg.did;
    var cell = document.getElementById(cellId);
    if (!cell) { return; }
    var formatted = formatValue(msg.value);
    cell.textContent = formatted;
    cell.title = typeof msg.value === "object" ? JSON.stringify(msg.value, null, 2) : String(msg.value);
    cell.classList.remove("flash-green");
    // Force reflow so the animation restarts
    void cell.offsetWidth;
    cell.classList.add("flash-green");
}

function filterTable() {
    var search = document.getElementById("dp-search").value.toLowerCase();
    var prioFilter = document.getElementById("dp-prio-filter").value;

    // Filter rows across all ECU group tables
    document.querySelectorAll(".ecu-group").forEach(function (group) {
        var visibleCount = 0;
        group.querySelectorAll("tbody tr").forEach(function (row) {
            var name = (row.dataset.name || "").toLowerCase();
            var did = (row.dataset.did || "").toLowerCase();
            var priority = row.dataset.priority || "";

            var matchSearch = !search || name.indexOf(search) !== -1 || did.indexOf(search) !== -1;
            var matchPrio = !prioFilter || priority === prioFilter;

            var visible = matchSearch && matchPrio;
            row.style.display = visible ? "" : "none";
            if (visible) visibleCount++;
        });

        // Hide entire ECU group if no rows match
        group.style.display = visibleCount > 0 ? "" : "none";

        // Auto-expand groups when searching
        if (search || prioFilter) {
            var collapse = group.querySelector(".collapse");
            if (collapse && !collapse.classList.contains("show") && visibleCount > 0) {
                new bootstrap.Collapse(collapse, {toggle: true});
            }
        }
    });
}

// Debounced engine schedule reload — waits 1 second after last change
var _reloadTimer = null;
function scheduleReload() {
    if (_reloadTimer) clearTimeout(_reloadTimer);
    _reloadTimer = setTimeout(function() { reloadEngineSchedule(); }, 1000);
    var status = document.getElementById("save-status");
    if (status) { status.textContent = "Changes pending..."; status.className = "ms-2 small text-warning"; }
}

async function reloadEngineSchedule() {
    var status = document.getElementById("save-status");
    try {
        var result = await apiCall("/api/engine/reload-schedule", "POST");
        if (status) { status.textContent = "Applied: " + result.polling + " polling"; status.className = "ms-2 small text-success"; }
        showToast("Engine reloaded: " + result.polling + " datapoints active", "success");
    } catch (e) {
        if (status) { status.textContent = "Reload failed"; status.className = "ms-2 small text-danger"; }
    }
}

async function setPriority(dpId, priority) {
    try {
        await apiCall("/api/datapoints/" + dpId, "PATCH", { poll_priority: parseInt(priority, 10) });
        var row = document.querySelector("tr[data-dp-id='" + dpId + "']");
        if (row) { row.dataset.priority = priority; }
        scheduleReload();
    } catch (e) {
        // error toast already shown by apiCall
    }
}

async function togglePolling(dpId, enabled) {
    try {
        await apiCall("/api/datapoints/" + dpId, "PATCH", { poll_enabled: enabled });
        scheduleReload();
    } catch (e) {
        var toggle = document.getElementById("poll-" + dpId);
        if (toggle) { toggle.checked = !enabled; }
    }
}

async function bulkSetPriority() {
    var priority = document.getElementById("bulk-priority-select").value;
    if (!priority) {
        showToast("Please select a priority value.", "warning");
        return;
    }
    var checked = document.querySelectorAll(".dp-check:checked");
    if (checked.length === 0) {
        showToast("No datapoints selected.", "warning");
        return;
    }
    var promises = [];
    checked.forEach(function (cb) {
        promises.push(setPriority(cb.value, priority));
    });
    await Promise.all(promises);
    // Update the inline selects in the table
    checked.forEach(function (cb) {
        var sel = document.getElementById("prio-sel-" + cb.value);
        if (sel) { sel.value = priority; }
        var row = document.querySelector("tr[data-dp-id='" + cb.value + "']");
        if (row) { row.dataset.priority = priority; }
    });
    showToast("Priority updated for " + checked.length + " datapoint(s). Reloading engine...", "info");
    await reloadEngineSchedule();
}

async function bulkSetPoll(enabled) {
    var checked = document.querySelectorAll(".dp-check:checked");
    if (checked.length === 0) {
        showToast("No datapoints selected.", "warning");
        return;
    }
    var promises = [];
    checked.forEach(function (cb) {
        promises.push(togglePolling(cb.value, enabled));
    });
    await Promise.all(promises);
    // Update the inline switches
    checked.forEach(function (cb) {
        var sw = document.getElementById("poll-" + cb.value);
        if (sw) { sw.checked = enabled; }
    });
    showToast("Polling " + (enabled ? "enabled" : "disabled") + " for " + checked.length + " datapoint(s). Reloading engine...", "info");
    await reloadEngineSchedule();
}

async function saveAndApply() {
    var btn = document.getElementById("btn-save-apply");
    btn.disabled = true;
    await reloadEngineSchedule();
    btn.disabled = false;
}

function toggleSelectAll(master) {
    var checkboxes = document.querySelectorAll(".dp-check");
    checkboxes.forEach(function (cb) {
        // Only toggle visible rows
        var row = cb.closest("tr");
        if (!row || row.style.display === "none") { return; }
        cb.checked = master.checked;
    });
}
