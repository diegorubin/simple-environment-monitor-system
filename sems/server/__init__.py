import tornado
import os

from sems import logger
from sems.logger import general

from sems.monitors.helpers import load_monitors
from sems.monitors import monitors as list_monitors
from sems.server.api.monitors import *
from sems.server.dashboard import Dashboard
from sems.server.static import Static

from sems.settings import SERVER_PORT, DEBUG


def make_app():
    app = tornado.web.Application(
        [
            (r"/", Dashboard),
            (r"/static/([\w_\.-]+)", Static),
            (r"/api/monitors", MonitorsHandler),
            (r"/api/monitors/positions", MonitorsPositionsHandler),
            (r"/api/monitors/(.+)/check", MonitorsCheckHandler),
            (r"/api/monitors/(\w+)/fields", MonitorsFieldsHandler),
            (r"/api/monitors/(.+)", MonitorsDestroyHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=DEBUG
    )
    return app


def start():

    logger.initialize_logging()

    app = make_app()
    app.listen(SERVER_PORT)

    load_monitors()
    for monitor in list_monitors:
        general.info("loading monitor type: " + monitor)

    general.info("starting server")

    tornado.ioloop.IOLoop.current().start()

