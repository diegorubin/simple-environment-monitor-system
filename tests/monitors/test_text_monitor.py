import unittest
import httpretty

from sems.monitors.text_monitor import TextMonitor


SERVICE_URL = "http://localhost:8888/healthcheck"


class TestTextMonitor(unittest.TestCase):

    def setUp(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, SERVICE_URL, body="LIVE")

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_alive(self):
        monitor = TextMonitor(SERVICE_URL, "LIVE");
        self.assertTrue(monitor.alive())

if __name__ == '__main__':
    unittest.main()

