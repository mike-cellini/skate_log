import sqlite3
import os
from activity import Activity
from person import Person


class Database:
    def __init__(self, db_path):
        db_exists = False
        if os.path.isfile(db_path):
            db_exists = True

        self.__con = sqlite3.connect(db_path)

        if not db_exists:
            self._create_database()

    def _create_database(self):
        cur = self.__con.cursor()
        cur.execute("CREATE TABLE person(name TEXT, birthdate TEXT)")
        cur.execute("""CREATE TABLE activity(
                            person TEXT,
                            date TEXT,
                            activity_type TEXT,
                            skate TEXT,
                            hours NUMERIC)""")
        self.__con.commit()

    def add_person(self, name, birthdate=None):
        cur = self.__con.cursor()
        person_exists = False
        for row in cur.execute("SELECT name FROM person"):
            if row[0] == name:
                person_exists = True

        if not person_exists:
            cur.execute("INSERT INTO person VALUES(?, ?)", (name, birthdate))

    def get_persons(self):
        cur = self.__con.cursor()
        rows = cur.execute("SELECT name, birthdate FROM person")

        persons = []
        for row in rows:
            persons.append(Person(row[0], row[1]))

        return persons

    def add_activity(self, name, date, activity_type, skate, hours):
        cur = self.__con.cursor()
        cur.execute("INSERT INTO activity VALUES(?, ?, ?, ?, ?)",
                    (name, date, activity_type, skate, hours))
        self.__con.commit()

    def get_activities_by_person(self, name):
        cur = self.__con.cursor()
        rows = cur.execute("""SELECT person, date, activity_type, skate, hours
                              FROM activity
                              WHERE person = ?""", (name,))
        activities = []
        for row in rows:
            activities.append(Activity(row[0], row[1], row[2], row[3], row[4]))

        return activities
