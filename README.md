#Simple Environment Monitor System
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

| Variable Name    | Description                              | Default Value          |
| ---------------- | ---------------------------------------- | ---------------------- |
| SEMS_DATABASE    | Complete path to file used like database | <current_path>/db.json |
| SEMS_SERVER_PORT | Port number where the server responds    | 8888                   |

![Sems](http://diegorubin.com/images/sems)

