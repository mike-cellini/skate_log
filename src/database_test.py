import unittest
import os
from database import Database


class DatabaseTests(unittest.TestCase):
    def test_create_database(self):
        name = 'test.db'
        Database(name)
        self.assertTrue(os.path.isfile(name))
        os.remove(name)

    def test_add_person(self):
        name = 'test.db'
        db = Database(name)
        person1 = "Person 1"
        db.add_person(person1)

        person1_count = 0
        for person in db.get_persons():
            if person[0] == person1:
                person1_count += 1
        self.assertEqual(person1_count, 1)

        db.add_person(person1)
        person1_count = 0
        for person in db.get_persons():
            if person[0] == person1:
                person1_count += 1
        self.assertEqual(person1_count, 1)
        os.remove(name)

    def test_add_activity(self):
        name = 'test.db'
        db = Database(name)
        db.add_activity('Person 1', '2023-01-01', 'Test Skate', 'Rent', '0.4')
        db.add_activity('Person 1', '2023-01-05', 'Test Skate', 'Rent', '0.4')
        db.add_activity('Person 2', '2023-01-05', 'Test Skate', 'Rent', '0.4')

        person1_activities = db.get_activities_by_person('Person 1')
        person2_activities = db.get_activities_by_person('Person 2')
        self.assertEqual(len(person1_activities), 2)
        self.assertEqual(len(person2_activities), 1)
        os.remove(name)


if __name__ == "__main__":
    unittest.main()
