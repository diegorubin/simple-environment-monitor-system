
var checked_monitors = [];

function updateMonitors(pollInterval) {
    $(".monitor-entry").each(function() {
        // console.log("Updating monitor ...");
        updateMonitor(this, pollInterval);
    });
}

function updateMonitor(element, pollInterval) {
    var monitor = $(element);
    var monitorLabel = monitor.find("span.component-name:first").text();

    // console.log("Monitor " + monitorLabel + " to be updated. Poll interval is pollInterval ...");

    $.get('/api/monitors/' + monitorLabel + '/check', function( response ) {
        // console.log("Received monitor response for " + monitorLabel + ". Poll interval = " + pollInterval + "Response is = " + response);

        if( response && response.data ) {
            var status = response.data.alive;
            var monitorHolder = monitor.find("span.component-status:first");

            if( status === true ) {
                monitorHolder.removeClass("unhealthy");
                monitorHolder.addClass("healthy");

                monitorHolder.html(
                    "<i class='fa fa-check'></i>Healthy"
                );
            }
            else {
                monitorHolder.removeClass("healthy");
                monitorHolder.addClass("unhealthy");

                monitorHolder.html(
                    "<i class='fa fa-times'></i>Unhealthy"
                );
            }
        }

        $("#summary").trigger("monitors.monitorUpdated", [ monitorLabel, status ]);

        setTimeout(function() {
            updateMonitor(element, pollInterval);
        }, pollInterval);
    });
}

function updateEnvStatus(monitor, status) {
    checked_monitors[monitor] = status;
    
    var summary = $("#summary");
    var alertBox = summary.find("div.alert:first");

    var overallStatus = true;

    for (let [key, value] of Object.entries(checked_monitors)) {
        if( value === false ) {
            overallStatus = false;
            break;
        }
    }

    alertBox.removeClass("d-none");

    if( overallStatus === true ) {
        alertBox.removeClass("alert-danger");
        alertBox.addClass("alert-success");

        alertBox.html("<i class='fa fa-check mr-1'></i>All Systems are Healthy!");
    }
    else {
        alertBox.removeClass("alert-success");
        alertBox.addClass("alert-danger");

        alertBox.html("<i class='fa fa-times mr-1'></i>Oops! It seems you have some issues to check!");
    }
}

(function() {

    let pollInterval = 10000;
    let metaPollInterval = $("meta[name='polling-interval]:first").attr("content");

    if( metaPollInterval ) {
        pollInterval = metaPollInterval;
    }

    $("#summary").on("monitors.monitorUpdated", function(event, monitor, status) {
        updateEnvStatus(monitor, status);
    });

    //console.log("Initializing monitors ...");
    updateMonitors(pollInterval);
})();