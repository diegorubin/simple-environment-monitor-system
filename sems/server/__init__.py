import tornado

from sems.server.api.monitors import MonitorsCheck, MonitorsCreate, MonitorsFields
from sems.server.dashboard import Dashboard
from sems.server.static import Static


def make_app():
    app = tornado.web.Application([
        (r"/", Dashboard),
        (r"/static/([\w_\.-]+)", Static),
        (r"/api/monitors", MonitorsCreate),
        (r"/api/monitors/(\w+)/check", MonitorsCheck),
        (r"/api/monitors/(\w+)/fields", MonitorsFields),
    ])
    return app
