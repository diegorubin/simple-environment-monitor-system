from abc import abstractmethod
import urllib2


class Base(object):

    def __init__(self, entrypoint):
        self.entrypoint = entrypoint

    @abstractmethod
    def alive(self):
        pass

    def get_content(self):
        return urllib2.urlopen(self.entrypoint).read()

