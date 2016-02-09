import tornado.web


class Dashboard(tornado.web.RequestHandler):

    def get(self):
        self.render("templates/dashboard.html")


