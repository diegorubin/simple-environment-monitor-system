from tinydb import TinyDB, Query
from sems.settings import TINY_DB_PATH


class Base(object):

    def __init__(self, **attributes):
        self.__dict__ = attributes
        self.db = TinyDB(TINY_DB_PATH)
        self.table = self.db.table(self.__class__.__name__)

    def all(self):
        monitors = []
        for elem in self.table.all():
            monitors.append(self.__class__(**elem))
        return monitors

    def load(self, label):
        query = Query()
        self.__dict__.update(self.table.search(query.label == label)[0])

    def save(self):
        attributes = self.get_attributes()
        if self.__new_record__():
            self.table.insert(attributes)
        else:
            query = Query()
            self.table.update(attributes, query.label == self.label)
        return True

    def destroy(self):
        query = Query()
        self.table.remove(eids=[self.table.search(query.label == self.label)[0].eid])

    def get_attributes(self):
        attributes = self.__dict__.copy()
        attributes.pop('db')
        attributes.pop('table')

        return attributes

    def __new_record__(self):
        query = Query()
        return len(self.table.search(query.label == self.label)) == 0
