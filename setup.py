from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="sems",
    version="0.0.7",
    url="http://github.com/diegorubin/simple-environment-monitor-system",
    author="Diego Rubin",
    author_email="rubin.diego@gmail.com",
    license="GPL2",
    scripts=['bin/sems-start'],
    include_package_data=True,
    description="A Simple Environment Monitor System",
    install_requires=reqs,
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages()
)

