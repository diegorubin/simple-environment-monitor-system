import tornado.web


class Static(tornado.web.RequestHandler):

    def get(self, static_file):
        self.render("static/%s" % static_file)
