# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import sys
sys.path.append(r'C:\Users\Hoyt\Documents\Code\HTML\NASCARFantasy')
from BackEnd.db.NASCARFanatasydb import NASCARSQL

class RacingrefscrapePipeline:
    def __init__(self):
        self.db = NASCARSQL()

    def process_item(self, item, spider):
        if spider.name == 'RaceOptions':
            try:
                valus = (int(item['number'][0]), item['name'][0], item['link'][0])
                print("""INSERT OR IGNORE INTO races(?,?,?)""", valus)
                self.db.cur.execute("""INSERT OR IGNORE INTO races VALUES (?,?,?)""", valus)
                self.db.con.commit()
            except:
                pass
        elif spider.name == 'RaceResults':
            print('-------------------------------------------------------------------------------------')
            valus = [int(item['car_number'][0]), item['driver'][0], int(item['position'][0])]
            print(valus)
            self.db.create_race_results_table(spider.track_name)
            print("""INSERT OR IGNORE INTO ? VALUES (?,?,?)""", valus)
            query = "INSERT OR IGNORE INTO {} VALUES (?,?,?)".format(spider.track_name)
            self.db.cur.execute(query, valus)
            self.db.con.commit()

        return item
