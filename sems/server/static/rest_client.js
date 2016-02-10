var RestClient = function(service) {
    var _this = this;
    _this.xhttp = new XMLHttpRequest();

    this.call = function(method, data) {
        _this.xhttp.open(method, service, true);
        _this.xhttp.onreadystatechange = function() {
            if(_this.xhttp.readyState == 4 && _this.xhttp.status == 200) {
                var data = JSON.parse(xhttp.responseText);
                if(_this.success) _this.success(data);
            }
        };
        _this.xhttp.send(data);
    };
};
