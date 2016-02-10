import sems, os

from sems.server import make_app
from sems.repository.monitor import Monitor

from tornado.escape import json_encode
from tornado.testing import AsyncHTTPTestCase

SERVICE_URL = "http://localhost:8888/healthcheck"


class TestMonitors(AsyncHTTPTestCase):

    def tearDown(self):
        if os.path.isfile(sems.repository.base.TINY_DB_PATH):
            os.remove(sems.repository.base.TINY_DB_PATH)

    def get_app(self):
        sems.repository.base.TINY_DB_PATH = "/tmp/tinydbtest.json"
        return make_app()

    def test_custom_fields(self):
        response = self.fetch('/api/monitors/TextMonitor/fields')
        self.assertEqual(response.code, 200)
        self.assertIn('expected', response.body)

    def test_create(self):
        body = json_encode({
            'type': 'TextMonitor', 'label': 'server',
            'url': SERVICE_URL,
            'data': {'expected': 'LIVE'}
        })
        response = self.fetch('/api/monitors', method='POST', body=body)
        self.assertEqual(response.code, 200)
        self.assertEqual(len(Monitor().all()), 1)

    def test_list(self):
        label = 'test'

        monitor = Monitor(label=label)
        monitor.save()

        response = self.fetch('/api/monitors')
        self.assertEqual(response.code, 200)
        self.assertIn(label, response.body)

