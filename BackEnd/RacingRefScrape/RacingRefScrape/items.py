# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RacingrefscrapeItem(scrapy.Item):
    name = scrapy.Field(default='NA')
    link = scrapy.Field(default='NA')
    pass
