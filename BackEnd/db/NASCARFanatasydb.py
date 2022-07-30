import sqlite3
import os
class NASCARSQL:
    def __init__(self):
        # self.con = sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db', 'NASCARFantasydb.db'))
        self.con = sqlite3.connect(r"C:\Users\Hoyt\Documents\Code\HTML\NASCARFantasy\BackEnd\db\NASCARFantasydb.db")
        self.cur = self.con.cursor()
        self.create_race_options_table()

    def create_race_options_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS races (number REAL PRIMARY KEY, name TEXT, link TEXT)""")

    def create_race_results_table(self, name):
        print("""CREATE TABLE IF NOT EXISTS ? (driver REAL PRIMARY KEY, position REAL, car_number REAL)""",(name,))
        print("CREATE TABLE IF NOT EXISTS {} (car_number REAL PRIMARY KEY, driver TEXT, position REAL)".format(name))
        self.cur.execute("CREATE TABLE IF NOT EXISTS {} (car_number REAL PRIMARY KEY, driver TEXT, position REAL)".format(name))
