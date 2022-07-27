# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class RacingrefscrapePipeline:
    def __init__(self):
        self.con = sqlite3.connect('NASCARFantasy.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXIST races(
        number REAL PRIMARY KEY,
        name TEXT,
        link TEXT)""")
    def process_item(self, item, spider):
        return item
