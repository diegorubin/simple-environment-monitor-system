from tinydb import TinyDB, Query

TINY_DB_PATH = "/var/db/sems/db.json"


class Base(object):

    def __init__(self, **attributes):
        self.__dict__ = attributes
        self.db = TinyDB(TINY_DB_PATH)
        self.table = self.db.table(self.__class__.__name__)

    def all(self):
        return self.table.all()

    def load(self, label):
        query = Query()
        self.__dict__.update(self.table.search(query.label == label)[0])

    def save(self):
        attributes = self.__dict__.copy()
        attributes.pop('db')
        attributes.pop('table')

        if self.__new_record__():
            self.table.insert(attributes)
        else:
            query = Query()
            self.table.update(attributes, query.label == self.label)
        return True

    def __new_record__(self):
        query = Query()
        return len(self.table.search(query.label == self.label)) == 0

