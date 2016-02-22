import unittest
import shutil
import os

from sems import settings
from sems import logger


class TestLogger(unittest.TestCase):

    def setUp(self):
        settings.LOG_PATH = "tests/log"

    def tearDown(self):
        shutil.rmtree("tests/log")

    def test_files_created(self):
        logger.initialize_logging()

        self.assertTrue(os.path.isfile("tests/log/sems.access.log"))
        self.assertTrue(os.path.isfile("tests/log/sems.application.log"))
        self.assertTrue(os.path.isfile("tests/log/sems.general.log"))

