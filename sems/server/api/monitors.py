from base import Base

from sems.repository.monitor import Monitor


class MonitorsCreate(Base):

    def post(self):

        monitor_type = self.get_argument('type')
        monitor_label = self.get_argument('label')

        monitor = Monitor(monitor_type=monitor_type, label=monitor_label)
        monitor.save()

        return {"monitor" : monitor.attributes}


class MonitorsCheck(Base):

    def get(self, label):
        monitor = Monitor()
        monitor.load(label)

        return {"monitor": monitor.attributes}

