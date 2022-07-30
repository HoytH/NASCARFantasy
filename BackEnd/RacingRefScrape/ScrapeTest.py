import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from BackEnd.RacingRefScrape.RacingRefScrape.spiders.RaceOptions import RaceOptions, RaceResults
from BackEnd.db.NASCARFanatasydb import NASCARSQL
import sys

spider_settings = get_project_settings()
process = CrawlerProcess(spider_settings)
process.crawl(RaceOptions)
process.start()

db = NASCARSQL()
input = db.cur.execute("""SELECT link, name FROM races""").fetchall()
for result in input:
    print(result)
    link = result[0]
    track_name = result[1].replace(' ', '_')
    if "twisted.internet.reactor" in sys.modules:
        del sys.modules["twisted.internet.reactor"]
    spider_settings = get_project_settings()
    process = CrawlerProcess(spider_settings)
    process.crawl(RaceResults, link = link, name=track_name)
    process.start()


