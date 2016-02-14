#!/usr/bin/env python
import tornado
from sems.server import make_app
from sems.settings import SERVER_PORT

if __name__ == '__main__':

    app = make_app()
    app.listen(SERVER_PORT)
    tornado.ioloop.IOLoop.current().start()
