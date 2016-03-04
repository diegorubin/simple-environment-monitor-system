import sys

try:
    from urllib import error
except ImportError:
    import urllib2 as error

from sems.monitors import *
from sems.utils import camel_to_snake_case


def check_alive(monitor_type, url, **data):
    module = "sems.monitors.%s" % (camel_to_snake_case(monitor_type))

    if module not in sys.modules:
        __import__(module)

    klass = getattr(sys.modules[module], monitor_type)
    monitor = klass(url, **data)

    try:
        return monitor.alive()
    except error.URLError:
        return False


def get_custom_fields(monitor_type):
    return monitors[monitor_type]['fields']

