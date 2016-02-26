try:
    from urllib import error
except ImportError:
    import urllib2 as error

from sems.monitors import Monitor
from sems.monitors.base import Base


@Monitor('Check Status HTTP', {
    'code': {'type': 'text'}
})
class HTTPStatusMonitor(Base):

    def alive(self):

        try:
            response = self.get_url_response()
            return response.getcode() == int(self.data['code'])
        except error.HTTPError as e:
            if hasattr(e, 'code'):
                return e.code == int(self.data['code'])
            else:
                return False
        except error.URLError:
            return False
