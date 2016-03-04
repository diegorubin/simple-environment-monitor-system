import telnetlib

from sems.monitors import Monitor
from sems.monitors.base import Base


@Monitor('Check Socket Port', {'port': {'type': 'text'}})
class SocketPortMonitor(Base):

    def alive(self):

        try:
            connection = telnetlib.Telnet(self.entrypoint, int(self.data['port']), 1)
            connection.close()
            return True
        except:
            return False
