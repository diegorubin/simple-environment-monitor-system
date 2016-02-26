import unittest
import httpretty

from sems.monitors.socket_port_monitor import SocketPortMonitor
from sems.monitors.helpers import check_alive


SERVICE_HOST = "localhost"
SERVICE_PORT = "8888"
SERVICE_URL = "http://%s:%s/" % (SERVICE_HOST, SERVICE_PORT)


class TestSocketPortMonitor(unittest.TestCase):

    def test_alive(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, SERVICE_URL, body="LIVE")

        monitor = SocketPortMonitor(SERVICE_HOST, port=SERVICE_PORT);
        self.assertTrue(monitor.alive())

        httpretty.disable()
        httpretty.reset()

    def test_out(self):
        monitor = SocketPortMonitor('hostnotexists', port=SERVICE_PORT);
        self.assertFalse(monitor.alive())

    def test_check_alive(self):
        httpretty.enable()
        httpretty.register_uri(httpretty.GET, SERVICE_URL, body="LIVE")

        self.assertTrue(check_alive('SocketPortMonitor', SERVICE_HOST, port='8888'))

        httpretty.disable()
        httpretty.reset()

