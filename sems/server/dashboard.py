# -*- coding: utf-8 -*-

import tornado.web

from sems.repository.monitor import Monitor


class Dashboard(tornado.web.RequestHandler):

    def get(self):
        monitor_types = [
            ('Selecione...', ''),
            ('Check HTTP Response Content', 'TextMonitor'),
            ('Check Status HTTP', 'HTTPStatusMonitor'),
            ('Check Socket Port', 'SocketPortMonitor')
        ]
        monitors = Monitor().ordered_by_position()
        self.render("dashboard.html", monitor_types=monitor_types, monitors=monitors)


