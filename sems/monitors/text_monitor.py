try:
    from urllib import error
except ImportError:
    import urllib2 as error

from sems.monitors.base import Base


class TextMonitor(Base):

    def alive(self):

        try:
            content = self.get_content().decode('utf-8')
            return self.data['expected'] in content
        except error.HTTPError:
            return False
        except error.URLError:
            return False
