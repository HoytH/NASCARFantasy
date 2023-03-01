import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
import sys
from BackEnd.RacingRefScrape.RacingRefSpider.spiders.RaceOptions import RaceOptions, RaceResults
from BackEnd.db.NASCARFanatasydb import NASCARSQL
from twisted.internet import reactor, defer


# spider_settings = get_project_settings()
# process = CrawlerProcess(spider_settings)
# process.crawl(RaceOptions)
# process.start()

psql = NASCARSQL()
psql.connect_db('nascarfantasy')
psql.cursor.execute("""SELECT link, name FROM races""")
results = psql.cursor.fetchall()
for result in results:
    link = result[0]
    track_name = result[1].replace(' ', '_')
    print('link:{}\n track_name:{}'.format(link, track_name))
    if "twisted.internet.reactor" in sys.modules:
        del sys.modules['twisted.internet.reactor']
        print('deleting reactor')

    spider_settings = get_project_settings()
    process = CrawlerProcess(spider_settings)
    process.crawl(RaceResults, link = link, name=track_name)
process.start()


