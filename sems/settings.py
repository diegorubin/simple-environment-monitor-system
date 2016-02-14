"""
Simple Environment Monitor System settings

For more information about available settings look at
https://github.com/diegorubin/simple-environment-monitor-system
"""
from os.path import abspath, curdir, join
from os import environ

TINY_DB_PATH = environ.get("SEMS_DATABASE", join(abspath(curdir), "db.json"))
SERVER_PORT = int(environ.get("SEMS_SERVER_PORT", "8888"))

