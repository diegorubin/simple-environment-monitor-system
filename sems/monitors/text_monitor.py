from base import Base


class TextMonitor(Base):

    def __init__(self, entrypoint, content_expected):
        super(self.__class__, self).__init__(entrypoint)
        self.__content_expected = content_expected

    def alive(self):
        content = self.get_content()
        print content
        return content == self.__content_expected


