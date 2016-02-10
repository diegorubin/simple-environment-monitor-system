import sys

from text_monitor import TextMonitor


def check_alive(monitor_type, url, **data):
    klass = getattr(sys.modules[__name__], monitor_type)
    monitor = klass(url, **data)

    return monitor.alive()
