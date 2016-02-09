from setuptools import setup, find_packages

setup(
    name = "sems",
    version = "0.1",
    summary = "Simple Environment Monitor System",
    url = "http://github.com/diegorubin/simple-environment-monitor-system",
    author = "Diego Rubin",
    author_email = "rubin.diego@gmail.com",
    license = "",
    scripts=['bin/sems-start'],
    install_requires = [
        "tornado",
        "tinydb"
    ],
    packages = find_packages()
)

