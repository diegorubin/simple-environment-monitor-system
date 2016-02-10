import sys

from text_monitor import TextMonitor

CUSTOM_FIELDS = {
    r'TextMonitor': {
        'expected': {'type': 'text'}
    }
}


def check_alive(monitor_type, url, **data):
    klass = getattr(sys.modules[__name__], monitor_type)
    monitor = klass(url, **data)

    return monitor.alive()


def get_custom_fields(monitor_type):
    return CUSTOM_FIELDS[monitor_type]
