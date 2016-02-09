import tornado.ioloop
import tornado.web


class Dashboard(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


