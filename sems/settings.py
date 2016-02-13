"""
Simple Environment Monitor System settings

For more information about available settings look at
https://github.com/diegorubin/simple-environment-monitor-system
"""
from os.path import abspath, curdir, join

TINY_DB_PATH = join(abspath(curdir), "db.json")
SERVER_PORT = 8888

