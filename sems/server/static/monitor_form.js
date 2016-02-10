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

};