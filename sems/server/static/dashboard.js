(function() {
    var monitorForm = new MonitorForm();
    monitorForm.init();

    var monitors = document.getElementsByClassName('monitor-entry');
    for(var i = 0; i < monitors.length; i++) {
        var monitor = new Monitor();
        monitor.init(monitors[i]);
    }
})();
