import tornado, os

from sems.server.api.monitors import MonitorsCheckHandler, MonitorsHandler, MonitorsFieldsHandler
from sems.server.dashboard import Dashboard
from sems.server.static import Static


def make_app():
    app = tornado.web.Application(
        [
            (r"/", Dashboard),
            (r"/static/([\w_\.-]+)", Static),
            (r"/api/monitors", MonitorsHandler),
            (r"/api/monitors/(\w+)/check", MonitorsCheckHandler),
            (r"/api/monitors/(\w+)/fields", MonitorsFieldsHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    return app
