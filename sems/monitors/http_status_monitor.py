from base import Base


class HTTPStatusMonitor(Base):

    def alive(self):
        response = self.get_url_response()
        return response.getcode() == int(self.data['code'])