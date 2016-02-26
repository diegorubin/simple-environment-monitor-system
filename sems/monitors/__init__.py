"""
List for registered monitors.
"""
monitors = {}


class Monitor(object):
    """
    Decorator to register a monitor.
    """
    def __init__(self, description, fields):
        self.description = description
        self.fields = fields

    def __call__(self, klass):
        monitors[klass.__name__] = {
            'fields': self.fields,
            'description': self.description
        }
        return klass
