import unittest
import sems
import os

from sems.repository.event import Event


class TestEvent(unittest.TestCase):

    def tearDown(self):
        os.remove(sems.repository.base.TINY_DB_PATH)

    def test_insert(self):
        event = Event(label="TEST")
        self.assertTrue(event.save())

    def test_all(self):
        event = Event(label="TEST")
        event.save()
        self.assertEqual(len(event.all()), 1)

    def test_find(self):
        Event(label="TEST").save()

        event = Event()
        event.load("TEST")
        self.assertEqual("TEST", event.label)

    def test_update(self):
        Event(label="TEST", name="name1").save()

        event = Event()
        event.load("TEST")
        event.name = "name2"
        event.save()

        event = Event()
        event.load("TEST")

        self.assertEqual(len(event.all()), 1)
        self.assertEqual(event.name, "name2")

    def test_destroy(self):
        Event(label="TEST", name="name1").save()

        event = Event()
        event.load("TEST")
        event.destroy()

        self.assertEqual(len(Event().all()), 0)
