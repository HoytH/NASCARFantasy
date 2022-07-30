import scrapy
from RacingRefScrape.items import RacingrefscrapeItem
from scrapy.loader import ItemLoader

class RaceOptions(scrapy.Spider):
    name = 'RaceOptions'
    start_urls = ['https://www.racing-reference.info/season-stats/2022/W/']

    def parse(self, response):
        for race in response.css('div.table-row'):
            l = ItemLoader(item=RacingrefscrapeItem(), selector=race)
            try:
                l.add_css('number', 'div.race-number>a::text')
                l.add_css('name','div.race-number>a::attr(title)')
                l.add_css('link','div.race-number>a::attr(href)')

                yield l.load_item()
            except:
                l.add_value('number', 'NONE')
                l.add_value('name', 'NONE')
                l.add_value('link', 'NONE')
                pass

class RaceResults(scrapy.Spider):
    name = 'RaceResults'
    def __init__(self, link, name):
        self.start_urls = [link]
        self.track_name = name

    def parse(selfself, response):
        for row in response.css('table.tb.race-results-tbl>tr'):
            l = ItemLoader(item=RacingrefscrapeItem(), selector=row)
            print(row)
            try:
                l.add_value('driver', row.css('td:nth-child(4)>a::text').extract()[0])
                l.add_value('position', row.css('td:nth-child(1)::text').extract()[0])
                l.add_value('car_number', row.css('td:nth-child(3)>a::text').extract()[0])
                print(l.load_item())

                yield l.load_item()
            except:
                print('exceptingggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
                l.add_value('driver', 'NONE')
                l.add_value('position', 'NONE')
                l.add_value('car_number', 'NONE')
                pass

