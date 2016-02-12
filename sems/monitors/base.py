from abc import abstractmethod

try:
    from urllib import request
except ImportError:
    import urllib2 as request


class Base(object):

    def __init__(self, entrypoint, **data):
        self.entrypoint = entrypoint
        self.data = data

    @abstractmethod
    def alive(self):
        pass

    def get_url_response(self):
        return request.urlopen(self.entrypoint)

    def get_content(self):
        return self.get_url_response().read()

