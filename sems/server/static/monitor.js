var Monitor = function() {
    var _this = this;

    this.init = function(element) {
        _this.label = element.getElementsByClassName("label")[0];

        _this.client = new RestClient('/api/monitors/' + _this.label + '/check');
        _this.client.success = function(data) {
            console.log(data);
        };

        setTimeout(function(){_this.check()}, 3000);
    };

    this.check = function() {
        _this.client.call("GET");
    };
};
