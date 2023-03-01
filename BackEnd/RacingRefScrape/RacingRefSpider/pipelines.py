# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.append(r'C:\Users\Hoyt\Documents\Code\HTML\NASCARFantasy')
from BackEnd.db.NASCARFanatasydb import NASCARSQL

class RacingrefSpiderPipeline:
    def __init__(self):
        self.db = NASCARSQL()
        self.db.connect_db('nascarfantasy')
        self.db.create_race_options_table()

    def process_item(self, item, spider):
        if spider.name == 'RaceOptions':
            try:
                valus = [int(item['number'][0]), item['name'][0], item['link'][0]]
                print("""INSERT INTO races VALUES (%s,%s,%s) ON CONFLICT DO NOTHING""", (valus),)
                self.db.cursor.execute("""INSERT INTO races VALUES (%s,%s,%s) ON CONFLICT DO Nothing""", (valus),)
            except:
                pass
        elif spider.name == 'RaceResults':
            print('-------------------------------------------------------------------------------------')
            valus = [int(item['car_number'][0]), item['driver'][0], int(item['position'][0])]
            print(valus)
            self.db.create_race_results_table(spider.track_name.lower())
            print("""INSERT INTO {} VALUES (%s,%s,%s) ON CONFLICT DO NOTHING""", (valus))
            query = "INSERT INTO {} VALUES (%s,%s,%s) ON CONFLICT DO NOTHING".format(spider.track_name)
            self.db.cursor.execute(query, (valus),)

        return item
