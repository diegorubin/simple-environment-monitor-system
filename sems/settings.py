"""
Simple Environment Monitor System settings

For more information about available settings look at
https://github.com/diegorubin/simple-environment-monitor-system
"""
from os.path import abspath, curdir, join
from os import environ

TINY_DB_PATH = environ.get("SEMS_DATABASE", join(abspath(curdir), "db.json"))
SERVER_PORT = int(environ.get("SEMS_SERVER_PORT", "8888"))
LOG_PATH = environ.get("SEMS_LOG_PATH", join(abspath(curdir), "log"))
LOG_LEVEL = environ.get("SEMS_LOG_LEVEL", "INFO")
DEBUG = environ.get("SEMS_DEBUG", "False") == "True"
WEB_POLLING_INTERVAL = environ.get("SEMS_WEB_POLLING_INTERVAL", "60000")
