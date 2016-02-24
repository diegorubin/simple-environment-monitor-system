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

    var groups = document.getElementsByClassName('group-wrapper');
    for (var i = 0; i < groups.length; i++) {
        Sortable.create(groups[i],{
            onUpdate: function(event) {
                var items = document.getElementsByClassName('monitor-label');
                var request = [];
                for(var item = 0; item < items.length; item++) {
                    request.push(items[item].innerHTML);
                }
                client.call('POST', {monitors: request})
            }
        });
    }

    /* init group menu */
    document.getElementById('groups-wrap').addEventListener('click', function(event){
        event.preventDefault();
        if(event.target.tagName === 'A') {
            var groups = document.getElementById('groups-wrap').getElementsByTagName('LI');
            for(var group in groups) {
                groups[group].className = '';
            }

            var containers = document.getElementsByClassName("group-wrapper");
            for(var container in containers) {
                containers[container].className = "group-wrapper hidden";
            }

            event.target.parentElement.className = "active";

            var group = event.target.dataset.group;
            var container = document.querySelectorAll("[data-container-group='" + group + "']")[0];
            container.className = "group-wrapper";
        }
    });
    document.getElementById('groups-wrap').getElementsByTagName('A')[0].click();

})();
