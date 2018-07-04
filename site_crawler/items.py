# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SiteCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsParagraph(scrapy.Item):
    title = scrapy.Field()
    paragraph_text = scrapy.Field()
    date = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
