Project discontinued in favor of [Lifeguard](https://github.com/LifeguardSystem) which turns out to be an evolution of SEMS.

# Simple Environment Monitor System

[![Join the chat at https://gitter.im/diegorubin/simple-environment-monitor-system](https://badges.gitter.im/diegorubin/simple-environment-monitor-system.svg)](https://gitter.im/diegorubin/simple-environment-monitor-system?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![PyPI version](https://badge.fury.io/py/sems.svg)](https://badge.fury.io/py/sems)
[![Build Status](https://travis-ci.org/diegorubin/simple-environment-monitor-system.svg)](https://travis-ci.org/diegorubin/simple-environment-monitor-system) 

## Installation

Directly from [PyPI](http://pypi.python.org/pypi/sems):

    pip install sems

Using pip but from source

    pip install git+https://github.com/diegorubin/simple-environment-monitor-system.git@master

or clone from the source (for the brave):

    git clone https://github.com/diegorubin/simple-environment-monitor-system.git
    cd simple-environment-monitor-system
    python setup.py install

## Usage

For installation using pip (PyPI or source)

    sems-start 

For installation from the source, go to the source project path and run

    python main.py
    
## Settings

To change settings use variables of environments.
The settings avaibles are:

| Variable Name             | Description                                                                      | Default Value            |
| ----------------          | -------------------------------------------------------------------------------- | ------------------------ |
| SEMS_DATABASE             | Complete path to file used like database.                                        | \<current_path\>/db.json |
| SEMS_SERVER_PORT          | Port number where the server responds.                                           | 8888                     |
| SEMS_LOG_LEVEL            | Log Level for application. Avaliable values are INFO, DEBUG, ERROR or CRITICAL.  | INFO                     |
| SEMS_LOG_PATH             | Path to log files.                                                               | \<current_path\>/log     |
| SEMS_DEBUG                | Run tornado application in debug mode. To enable uses True as value.             | False                    |
| SEMS_WEB_POLLING_INTERVAL | Monitor polling interval. Default value is one minute.                           | 60000                    |

![Sems](http://diegorubin.com/images/sems)

