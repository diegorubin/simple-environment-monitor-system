import os

from tornado.log import LogFormatter
from tornado.log import logging

from sems import settings

general = logging.getLogger('tornado.general')
application = logging.getLogger('tornado.application')
access = logging.getLogger('tornado.access')


def initialize_logging():

    for stream_name in ['access', 'general', 'application']:
        stream = logging.getLogger("tornado.%s" % stream_name)

        stream.setLevel(getattr(logging, settings.LOG_LEVEL))
        if not os.path.exists(settings.LOG_PATH):
            os.makedirs(settings.LOG_PATH)

        channel = logging.handlers.RotatingFileHandler(
            filename=os.path.join(settings.LOG_PATH, "sems.%s.log" % stream_name),
        )

        channel.setFormatter(LogFormatter(color=True))
        stream.addHandler(channel)

