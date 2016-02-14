import sems, os

from sems.server import make_app
from sems.repository.monitor import Monitor

from tornado.testing import AsyncHTTPTestCase


class TestDashboard(AsyncHTTPTestCase):

    def tearDown(self):
        if os.path.isfile(sems.repository.base.TINY_DB_PATH):
            os.remove(sems.repository.base.TINY_DB_PATH)

    def get_app(self):
        return make_app()

    def test_dashboard(self):
        label = "server.test"
        monitor = Monitor(label=label, url='http://server.com')
        monitor.save()

        response = self.fetch('/')

        self.assertEqual(response.code, 200)
        self.assertIn(label, response.body)
        self.assertIn('TextMonitor', response.body)
