# -*- coding: utf-8 -*-

import tornado.web

from sems.monitors import monitors as list_monitors
from sems.repository.monitor import Monitor
from sems.settings import WEB_POLLING_INTERVAL

from sems import VERSION


class Dashboard(tornado.web.RequestHandler):

    def get(self):

        monitor_types = [
            ('Select...', '')
        ]

        for monitor in list_monitors:
            item = (list_monitors[monitor]['description'], monitor)
            monitor_types.append(item)

        monitors = {}
        for monitor in Monitor().ordered_by_position():
            if hasattr(monitor, "group"):
                group = monitor.group
            else:
                group = ""

            if group not in monitors:
                monitors[group] = []
            monitors[group].append(monitor)

        groups = set([monitor for monitor in monitors])

        self.render("dashboard.html",
                    monitor_types=monitor_types,
                    groups_monitors=monitors,
                    groups=groups,
                    polling_interval=WEB_POLLING_INTERVAL,
                    version=VERSION)
