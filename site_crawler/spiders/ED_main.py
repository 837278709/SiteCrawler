# -*- coding: utf-8 -*-
from datetime import datetime
import scrapy
from scrapy.loader import ItemLoader
from site_crawler.items import NewsParagraph


class EdMainSpider(scrapy.Spider):
    name = 'ED_main'
    allowed_domains = ['inara.cz']
    start_urls = ['http://inara.cz/']

    def parse(self, response):
        l = ItemLoader(item=NewsParagraph(), response=response)
        l.add_xpath(
            'title', '/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[2]/h3[1]/text()')
        l.add_xpath(
            'date', '/html[1]/body[1]/div[2]/div[1]/div[3]/div[1]/div[2]/h3[1]/div[1]/text()')
        l.add_css('paragraph_text', 'div.clear > p::text')
        l.add_value('last_updated', datetime.today())
        rv = l.load_item()
        return rv
