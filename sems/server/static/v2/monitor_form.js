(function() {


    function loadCustomFields() {
        var selectedType = $("#monitorType").val();

        if(selectedType) {
            var url = '/api/monitors/' + selectedType + '/fields';

            $("#custom-fields").html('');

            $.get(url, function( customFields ) {
                if( customFields && customFields.data && 
                    customFields.data.fields) {
                    
                    for( var field in customFields.data.fields ) {

                        var template = $("#custom-field-template").html();

                        console.log(field);
                        console.log(customFields.data.fields[field].type);

                        template = template.replace(/#field_name#/g, field);
                        template = template.replace(/#field_type#/g, customFields.data.fields[field].type);

                        $("#custom-fields").append(template);
                    }
                }
            });
        }
    }

    /**
     * Initialize modal
     */
    $("#newMonitorModal").on("show.bs.modal", function() {
        loadCustomFields();
    });

    $("#newMonitorModal").on("hide.bs.modal	", function() {
        $("#newMonitorForm")[0].reset();
        $("#newMonitorForm").removeClass("was-validated");
    });

    $("#monitorType").on("change", function() {
        loadCustomFields();
    });

    /**
     * Save new monitor     * 
     */
    $("#save-new-monitor").on('click', function () {
                
        if($("#newMonitorForm")[0].checkValidity()) {
            var newMonitor = {};
            
            newMonitor.url = $("#monitorUrl").val();
            newMonitor.monitor_type = $("#monitorType").val();
            newMonitor.label = $("#monitorLabel").val();
            newMonitor.group = $("#monitorGroup").val();
            newMonitor.data = {};

            $("#custom-fields :input").each(function() {
                var input = $(this);
                
                newMonitor.data[input.attr('id')] = input.val();
            });

            $.post('/api/monitors', JSON.stringify(newMonitor))
                .done(function() {
                    window.location.reload();
                });

        } else {
            $("#newMonitorForm").addClass("was-validated");
        }
    });

})();
