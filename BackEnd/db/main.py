import sqlite3

class db:
    def __init__(self):
        self.con = sqlite3.connect('NASCARFantasy.db')
        self.cur = self.con.cursor()

        def create_table(self):
            self.cur.execute("""CREATE TABLE IF NOT EXIST races(
            number REAL PRIMARY KEY,
            name TEXT,
            link TEXT)""")
