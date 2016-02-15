(function() {
    var monitorForm = new MonitorForm();
    monitorForm.init();

    /* init pooling */
    var monitors = document.getElementsByClassName('monitor-entry');
    for(var i = 0; i < monitors.length; i++) {
        var monitor = new Monitor();
        monitor.init(monitors[i]);
    }

    /* init drangNdrop */
    var client = new RestClient('/api/monitors/positions');
    var monitorsList = document.getElementById('monitors');
    Sortable.create(monitorsList,{
        onUpdate: function(event) {
            var items = document.getElementsByClassName('monitor-label');
            var request = [];
            for(var item = 0; item < items.length; item++) {
                request.push(items[item].innerHTML);
            }
            client.call('POST', {monitors: request})
        }
    });

})();
