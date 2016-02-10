from abc import abstractmethod
import urllib2


class Base(object):

    def __init__(self, entrypoint, **data):
        self.entrypoint = entrypoint
        self.data = data

    @abstractmethod
    def alive(self):
        pass

    def get_content(self):
        return urllib2.urlopen(self.entrypoint).read()

