import sys
import urllib2

from text_monitor import TextMonitor
from http_status_monitor import HTTPStatusMonitor
from socket_port_monitor import SocketPortMonitor

CUSTOM_FIELDS = {
    r'TextMonitor': {
        'expected': {'type': 'text'}
    },
    r'HTTPStatusMonitor': {
        'code': {'type': 'text'}
    },
    r'SocketPortMonitor': {
        'port': {'type': 'text'}
    }
}


def check_alive(monitor_type, url, **data):
    klass = getattr(sys.modules[__name__], monitor_type)
    monitor = klass(url, **data)

    try:
        return monitor.alive()
    except urllib2.URLError, e:
        return False


def get_custom_fields(monitor_type):
    return CUSTOM_FIELDS[monitor_type]

