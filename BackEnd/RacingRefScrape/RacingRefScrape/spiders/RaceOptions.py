import scrapy
from RacingRefScrape.items import RacingrefscrapeItem
from scrapy.loader import ItemLoader

class RaceOptions(scrapy.Spider):
    name = 'RaceOptions'
    start_urls = ['https://www.racing-reference.info/season-stats/2022/W/']

    def parse(selfself, response):
        for race in response.css('div.table-row'):
            l = ItemLoader(item=RacingrefscrapeItem(), selector=race)
            try:
                l.add_css('name','div.track.W>a::attr(title)')
                l.add_css('link','div.track.W>a::attr(href)')
                yield l.load_item()
            except:
                l.add_value('name', 'NONE')
                l.add_value('link', 'NONE')
                pass

