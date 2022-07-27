import scrapy
from scrapy.crawler import CrawlerProcess
from RacingRefScrape.spiders.RaceOptions import RaceOptions

process = CrawlerProcess()
process.crawl(RaceOptions)
process.start()
