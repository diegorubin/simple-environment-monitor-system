from setuptools import setup, find_packages

setup(
    name = "sems",
    version = "0.0.3",
    url = "http://github.com/diegorubin/simple-environment-monitor-system",
    author = "Diego Rubin",
    author_email = "rubin.diego@gmail.com",
    license = "",
    scripts=['bin/sems-start'],
    include_package_data= True,
    install_requires = [
        "tornado",
        "tornado_json",
        "tinydb"
    ],
    packages = find_packages()
)

