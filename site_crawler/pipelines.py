# -*- coding: utf-8 -*-
# from itemadapter import ItemAdapter
import pymongo


class MongoPipeline(object):

    collection_name = 'galnet_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'localhost'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'test_db')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


class SiteCrawlerPipeline:
    def process_item(self, item, spider):
        item['paragraph_text'] = list(map(
            lambda line: line.rstrip('\r'), item.get('paragraph_text')))
        return item
