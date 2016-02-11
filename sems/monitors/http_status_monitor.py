import urllib2

from base import Base


class HTTPStatusMonitor(Base):

    def alive(self):

        try:
            response = self.get_url_response()
            return response.getcode() == int(self.data['code'])
        except urllib2.HTTPError, e:
            if hasattr(e, 'code'):
                return e.code == int(self.data['code'])
            else:
                return False
        except urllib2.URLError:
            return False
