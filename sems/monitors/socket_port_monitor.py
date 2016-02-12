import telnetlib

from sems.monitors.base import Base


class SocketPortMonitor(Base):

    def alive(self):

        try:
            connection = telnetlib.Telnet(self.entrypoint, int(self.data['port']), 1)
            connection.close()
            return True
        except:
            return False
