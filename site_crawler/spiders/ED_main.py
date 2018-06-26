# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from site_crawler.items import NewsParagraph


class EdMainSpider(scrapy.Spider):
    name = 'ED_main'
    allowed_domains = ['inara.cz']
    start_urls = ['http://inara.cz/']

#     def parse(self, response):
#         l = ItemLoader(item=NewsParagraph(), response=response)
#         l.add_css('lines', 'div.clear > p::text')
#         return l.load_item()

    def parse(self, response):
        p_n = 0
        lines = response.css('div.clear > p::text').extract()
        np = NewsParagraph()
        for i in lines:
            p_n += 1
            item = NewsParagraph(paragraph_text=i,
                                 paragraph_number=p_n)
            yield item
#             yield {
#                 'text': i,
#                 "paragraph number ": p_n,
#             }
