# -*- coding: utf-8 -*-

import tornado.web

from sems.repository.monitor import Monitor


class Dashboard(tornado.web.RequestHandler):

    def get(self):
        monitor_types = [
            ('Selecione...', ''),
            ('Checar Conteúdo', 'TextMonitor'),
            ('Checar Status HTTP', 'HTTPStatusMonitor')
        ]
        monitors = Monitor().all()
        self.render("dashboard.html", monitor_types=monitor_types, monitors=monitors)


