var MonitorForm = function() {
    var _this = this;
    _this.hidden = true;

    this.init = function() {
        _this.form = document.getElementById('form-monitor');
        _this.form.onsubmit = function(event) {
            event.preventDefault();
        };

        _this.formWrap = document.getElementById('form-wrap-monitor');

        _this.btnNewMonitor = document.getElementById('new-monitor');
        _this.btnNewMonitor.onclick = function(event) {
            event.preventDefault();
            _this.toggleForm();
        };

        _this.slMonitorType = document.getElementById('monitor-type');
        _this.slMonitorType.onchange = function(event) {
            _this.getCustomFields();
        };

        _this.dvCustomFields = document.getElementById('custom-fields');

        _this.getCustomFields();
    };

    this.save = function() {

    };

    this.toggleForm = function() {
        if(_this.hidden) {
            _this.formWrap.className='';
        } else {
            _this.formWrap.className='hidden';
        }
        _this.hidden = !_this.hidden;
    };

    this.getCustomFields = function() {
        var value = _this.slMonitorType.value;

        if(value != "") {
            var client = new RestClient('/api/monitors/' + value + '/fields' );
            client.success = function(data) {
                data = data.data;
                _this.dvCustomFields.innerHTML = '';
                for(var field in data.fields) {
                    var span = document.createElement('label');
                    span.innerHTML = field;

                    var input = document.createElement('input');
                    input.type = data.fields[field].type;
                    input.name = field;

                    _this.dvCustomFields.appendChild(span);
                    _this.dvCustomFields.appendChild(input);
                }
            };
            client.call('GET')
        }
    };

};