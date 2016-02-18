# -*- coding: utf-8 -*-

import tornado.web

from sems.repository.monitor import Monitor


class Dashboard(tornado.web.RequestHandler):

    def get(self):

        monitor_types = [
            ('Select...', ''),
            ('Check HTTP Response Content', 'TextMonitor'),
            ('Check Status HTTP', 'HTTPStatusMonitor'),
            ('Check Socket Port', 'SocketPortMonitor')
        ]

        monitors = {}
        for monitor in Monitor().ordered_by_position():
            if hasattr(monitor, "group"):
                group = monitor.group
            else:
                group = ""

            if group not in monitors:
                monitors[group] = []
            monitors[group].append(monitor)

        groups = [monitor.group for monitor in monitors if hasattr(monitor, 'group')]

        self.render("dashboard.html", monitor_types=monitor_types, groups_monitors=monitors, groups=groups)


