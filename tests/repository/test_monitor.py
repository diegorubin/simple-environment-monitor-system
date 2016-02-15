import unittest

from sems.repository.monitor import Monitor


class TestMonitor(unittest.TestCase):

    def test_get_default_position(self):
        monitor = Monitor()
        self.assertEqual(monitor.get_position(), 0)

    def test_get_custom_position(self):
        monitor = Monitor(position=2)
        self.assertEqual(monitor.get_position(), 2)
