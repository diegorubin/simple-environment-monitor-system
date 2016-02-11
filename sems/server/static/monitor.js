var Monitor = function() {
    var _this = this;

    this.init = function(element) {
        _this.label = element.getElementsByClassName("monitor-label")[0].innerHTML;
        _this.status = element.getElementsByClassName("monitor-status")[0];

        _this.client = new RestClient('/api/monitors/' + _this.label + '/check');
        _this.client.success = function(response) {
            _this.status.innerHTML = (response.data.alive ? 'LIVE' : 'OUT');
            element.className = (response.data.alive ? 'monitor-entry live' : 'monitor-entry out');
        };

        _this.lnkRemove = element.getElementsByClassName("monitor-remove")[0];
        _this.lnkRemove.onclick = function(event) {
            event.preventDefault();

            var client = new RestClient('/api/monitors/' + _this.label);
            client.success = function() {
                window.location.reload();
            };
            client.call('DELETE');
        };

        if(_this.label && _this.label != '') _this.check();
    };

    this.check = function() {
        _this.client.call("GET");
        setTimeout(function(){_this.check()}, 60000);
    };
};
