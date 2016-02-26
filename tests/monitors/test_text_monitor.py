import unittest
import httpretty

from sems.monitors.text_monitor import TextMonitor
from sems.monitors.helpers import check_alive


SERVICE_URL = "http://localhost:8888/healthcheck"


class TestTextMonitor(unittest.TestCase):

    def setUp(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, SERVICE_URL, body="LIVE")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_alive(self):
        monitor = TextMonitor(SERVICE_URL, expected='LIVE');
        self.assertTrue(monitor.alive())

    def test_out(self):
        monitor = TextMonitor(SERVICE_URL+"/false", expected='LIVE');
        self.assertFalse(monitor.alive())

    def test_check_alive(self):
        self.assertTrue(check_alive('TextMonitor', SERVICE_URL, expected='LIVE'))


