from base import Base

from tornado.escape import json_decode

from sems.repository.monitor import Monitor
from sems.monitors import check_alive, get_custom_fields


class MonitorsCreate(Base):

    def post(self):

        json_request = json_decode(self.request.body)
        monitor = Monitor(**json_request)
        monitor.save()

        self.success({"monitor": monitor.get_attributes()})


class MonitorsCheck(Base):

    def get(self, label):
        monitor = Monitor()
        monitor.load(label)

        alive = check_alive(monitor.monitor_type, monitor.url, monitor.data)
        self.success({"monitor": monitor.get_attributes(), "alive": alive})


class MonitorsFields(Base):

    def get(self, monitor_type):

        self.success({"fields": get_custom_fields(monitor_type)})

