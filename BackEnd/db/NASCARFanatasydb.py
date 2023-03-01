import psycopg2
import os
class NASCARSQL:
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'postgres'
        self.password = '159753'
        self.port_id = 5432
    def connect_db(self, db_name):
        try:
            db = psycopg2.connect(host=self.hostname,
            dbname=db_name,
            user=self.username,
            password=self.password,
            port=self.port_id)
            db.autocommit = True
            cursor = db.cursor()
            self.db, self.cursor = [db,cursor]
        except Exception as error:
            print('not connected')
            print(error)

    def create_schema(self):
        self.connect_db('postgres')
        self.cursor.execute('DROP DATABASE IF EXISTS nascarfantasy;')
        self.cursor.execute('CREATE DATABASE nascarfantasy;')
        self.db.close()

    def create_race_options_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS races (number REAL PRIMARY KEY, name TEXT, link TEXT)""")

    def create_race_results_table(self, name):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS \"{}\" (car_number REAL PRIMARY KEY, driver TEXT, position REAL)".format(name))

    def create_user_table(self, name):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user_teams (user TEXT PRIMARY KEY, drivers TEXT)".format(name))
#
# a = NASCARSQL()
# a.connect_db('nascarfantasy')
# valus = ([1, 'test', 'test'])
# print("""INSERT INTO races(%s,%s,%s) ON CONFLICT DO NOTHING/UPDATE""", (valus))
# a.cursor.execute("""INSERT INTO races VALUES (%s,%s,%s) ON CONFLICT DO NOTHING""", (valus))

# a.create_race_results_table('Daytona 500')