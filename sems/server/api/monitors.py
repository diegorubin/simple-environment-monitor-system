from sems.server.api.base import Base

from tornado.escape import json_decode

from sems.repository.monitor import Monitor
from sems.monitors.helpers import check_alive, get_custom_fields
from sems.logger import application


class MonitorsHandler(Base):

    def get(self):
        monitors = []

        for monitor in Monitor().all():
            monitors.append(monitor.get_attributes())

        self.success({'monitors': monitors})

    def post(self):

        application.info("creating monitor with attributes %s" % self.request.body)
        json_request = json_decode(self.request.body)
        monitor = Monitor(**json_request)
        monitor.save()

        self.success({"monitor": monitor.get_attributes()})


class MonitorsPositionsHandler(Base):

    def post(self):
        json_request = json_decode(self.request.body)

        for index, label in enumerate(json_request['monitors']):
            monitor = Monitor()
            monitor.load(label)
            monitor.position = index
            monitor.save()

        self.success(json_request)


class MonitorsDestroyHandler(Base):

    def delete(self, label):
        monitor = Monitor()
        monitor.load(label)

        application.info("removing monitor %s" % label)

        self.success({"monitor": monitor.get_attributes(), "destroy": monitor.destroy()})


class MonitorsCheckHandler(Base):

    def get(self, label):
        monitor = Monitor()
        monitor.load(label)

        alive = check_alive(monitor.monitor_type, monitor.url, **monitor.data)
        self.success({"monitor": monitor.get_attributes(), "alive": alive})


class MonitorsFieldsHandler(Base):

    def get(self, monitor_type):

        self.success({"fields": get_custom_fields(monitor_type)})

