import scrapy

class RaceOptions(scrapy.Spider):
    name = 'RaceOptions'
    start_urls = ['https://www.racing-reference.info/season-stats/2022/W/']

    def parse(selfself, response):
        for race in response.css('div.table-row'):
            yield {
                'name': race.css('div.track.W>a').attrib['title'],
                'link': race.css('div.track.W>a').attrib['href']
            }
