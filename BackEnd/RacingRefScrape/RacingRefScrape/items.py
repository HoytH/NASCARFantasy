# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RacingrefscrapeItem(scrapy.Item):
    number = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()

    driver = scrapy.Field()
    position = scrapy.Field()
    car_number = scrapy.Field()
