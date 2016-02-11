var MonitorForm = function() {
    var _this = this;
    _this.hidden = true;

    this.init = function() {
        _this.form = document.getElementById('form-monitor');

        _this.form.onsubmit = function(event) {
            event.preventDefault();
            if(_this.lblMonitor.value) {
                _this.save();
            } else {
                alert('Label is empty');
            }
        };

        _this.lblMonitor = document.getElementById('monitor-label');

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
        var data = {};
        data.url = document.getElementById('monitor-url').value;
        data.monitor_type = _this.slMonitorType.value;
        data.label = _this.lblMonitor.value;
        data.data = {};

        var customFields = _this.dvCustomFields.getElementsByTagName('input');
        for(var field in customFields) {
            var customField = customFields[field];
            data.data[customField.name] = customField.value;
        }

        var client = new RestClient('/api/monitors');
        client.success = function(response) {
            window.location.reload();
        };
        client.call('POST', data);

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
        _this.dvCustomFields.innerHTML = '';

        if(value != "") {
            var client = new RestClient('/api/monitors/' + value + '/fields' );
            client.success = function(data) {
                data = data.data;
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