import sys
import os

try:
    from urllib import error
except ImportError:
    import urllib2 as error

from sems.monitors import *
from sems.settings import TINY_DB_PATH
from sems.utils import camel_to_snake_case

external_monitors = []

def load_monitors():
    for f in os.listdir(os.path.join(os.path.dirname(__file__))):
        if(f.endswith("_monitor.py")):
            module = "sems.monitors.%s" % (camel_to_snake_case(f.replace('.py', '')))
            if module not in sys.modules:
                __import__(module)

    external_monitor_path = os.path.join(os.path.dirname(TINY_DB_PATH))
    sys.path.append(external_monitor_path)
    for f in os.listdir(os.path.join(external_monitor_path, 'external')):
        if(f.endswith("_monitor.py")):
            monitor = f.replace('.py', '')
            external_monitors.append(monitor)
            module = "external.%s" % (monitor)
            if module not in sys.modules:
                __import__(module)

def check_alive(monitor_type, url, **data):
    monitor_type_module = camel_to_snake_case(monitor_type)
    if monitor_type_module in external_monitors:
        module = "external.%s" % (monitor_type_module)
    else:
        module = "sems.monitors.%s" % (monitor_type_module)

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

