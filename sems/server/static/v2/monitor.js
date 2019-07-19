var Monitor = function() {
    var _this = this;

    this.init = function(element) {

        _this.interval = 60000;
        var interval = document.getElementsByClassName('polling-interval')[0];
        if (interval) {
            _this.interval = interval.getAttribute('content');
        }
        _this.label = element.getElementsByClassName("component-name")[0].innerHTML;
        _this.status = element.getElementsByClassName("component-status")[0];

        _this.client = new RestClient('/api/monitors/' + _this.label + '/check');

        _this.client.success = function(response) {
            _this.status.innerHTML = (response.data.alive ? 
                '<i class="fa fa-check"></i>Healthy' : '<i class="fa fa-times"></i>Unhealthy'
            );
            _this.status.classname = (response.data.alive ? 'component-status healthy mb-1' : 'component-status unhealthy mb-1');
        };

        // _this.lnkRemove = element.getElementsByClassName("monitor-remove")[0];
        // _this.lnkRemove.onclick = function(event) {
        //     event.preventDefault();

        //     var client = new RestClient('/api/monitors/' + _this.label);
        //     client.success = function() {
        //         window.location.reload();
        //     };
        //     client.call('DELETE');
        // };

        if(_this.label && _this.label != '') _this.check();
    };

    this.check = function() {
        _this.client.call("GET");
        setTimeout(function(){_this.check()}, _this.interval);
    };
};
