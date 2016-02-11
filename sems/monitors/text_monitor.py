import urllib2
from base import Base


class TextMonitor(Base):

    def alive(self):

        try:
            content = self.get_content()
            return content == self.data['expected']
        except urllib2.HTTPError:
            return False
        except urllib2.URLError:
            return False
