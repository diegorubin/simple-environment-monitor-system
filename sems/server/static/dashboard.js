(function() {
    var monitorForm = new MonitorForm();
    monitorForm.init();

    var monitors = document.getElementsByClassName('monitor-entry');
    console.log(monitors);
    for(var i = 0; i < monitors.lenght; i++) {
        var monitor = new Monitor();
        monitor.init(monitors[i]);
    }
})();
