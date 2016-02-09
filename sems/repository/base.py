from tinydb import TinyDB, Query

TINY_DB_PATH = "/var/db/sems/db.json"


class Base(object):

    def __init__(self, **attributes):
        self.db = TinyDB(TINY_DB_PATH)
        self.table = self.db.table(self.__class__.__name__)
        self.attributes = attributes

    def all(self):
        return self.table.all()

    def load(self, label):
        query = Query()
        self.attributes = self.table.search(query.label == label)[0]

    def save(self):
        if self.__new_record__():
            self.table.insert(self.attributes)
        else:
            query = Query()
            self.table.update(self.attributes, query.label == self.label)
        return True

    def __getattr__(self, item):
        if item in self.attributes:
            return self.attributes.get(item)
        else:
            self.__getattribute__(item)

    def __new_record__(self):
        query = Query()
        return len(self.table.search(query.label == self.label)) == 0

