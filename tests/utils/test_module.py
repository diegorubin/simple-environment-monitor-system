import unittest

from sems.utils import *


class TestModule(unittest.TestCase):

    def test_camel_to_snake_case(self):
        self.assertEqual(camel_to_snake_case("HTTPStatusMonitor"), "http_status_monitor")

