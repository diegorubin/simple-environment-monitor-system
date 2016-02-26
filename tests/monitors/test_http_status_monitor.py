import unittest
import httpretty

from sems.monitors.http_status_monitor import HTTPStatusMonitor
from sems.monitors.helpers import check_alive


SERVICE_URL = "http://localhost:8888/healthcheck"


class TestHTTPStatusMonitor(unittest.TestCase):

    def setUp(self):
        httpretty.enable()

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def test_alive(self):
        httpretty.register_uri(httpretty.GET, SERVICE_URL, status=200)
        monitor = HTTPStatusMonitor(SERVICE_URL, code='200');
        self.assertTrue(monitor.alive())

    def test_out(self):
        monitor = HTTPStatusMonitor(SERVICE_URL+"/false", status='200');
        self.assertFalse(monitor.alive())

    def test_404_status(self):
        httpretty.register_uri(httpretty.GET, SERVICE_URL, status=404)
        monitor = HTTPStatusMonitor(SERVICE_URL, code='404');
        self.assertTrue(monitor.alive())

    def test_422_status(self):
        httpretty.register_uri(httpretty.GET, SERVICE_URL, status=422)
        monitor = HTTPStatusMonitor(SERVICE_URL, code='422');
        self.assertTrue(monitor.alive())

    def test_expected_500_status(self):
        httpretty.register_uri(httpretty.GET, SERVICE_URL, status=500)
        monitor = HTTPStatusMonitor(SERVICE_URL, code='500');
        self.assertTrue(monitor.alive())

    def test_not_expected_500_status(self):
        httpretty.register_uri(httpretty.GET, SERVICE_URL, status=500)
        monitor = HTTPStatusMonitor(SERVICE_URL, code='200');
        self.assertFalse(monitor.alive())

    def test_check_alive(self):
        httpretty.register_uri(httpretty.GET, SERVICE_URL, status=200)
        self.assertTrue(check_alive('HTTPStatusMonitor', SERVICE_URL, code='200'))

