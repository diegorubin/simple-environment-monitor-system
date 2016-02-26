import sys

try:
    from urllib import error
except ImportError:
    import urllib2 as error

from sems.monitors import monitors

# TODO Github Issue #5 import dynamically
from sems.monitors.http_status_monitor import HTTPStatusMonitor
from sems.monitors.socket_port_monitor import SocketPortMonitor
from sems.monitors.text_monitor import TextMonitor


def check_alive(monitor_type, url, **data):
    klass = getattr(sys.modules[__name__], monitor_type)
    monitor = klass(url, **data)

    try:
        return monitor.alive()
    except error.URLError:
        return False


def get_custom_fields(monitor_type):
    return monitors[monitor_type]
