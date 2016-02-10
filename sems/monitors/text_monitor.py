from base import Base


class TextMonitor(Base):

    def alive(self):
        content = self.get_content()
        return content == self.data['expected']

