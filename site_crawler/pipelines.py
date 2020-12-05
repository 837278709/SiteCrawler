# -*- coding: utf-8 -*-
# from itemadapter import ItemAdapter
import motor.motor_asyncio
import asyncio

class MongoPipeline(object):

    collection_name = 'galnet_news'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://localhost:27017'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'test_db')
        )

    def open_spider(self, spider):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    async def insert_item(self):
        document = {'key': 'value'}
        result = await self.db.test_collection.insert_one(document)
        print('result %s' % repr(result.inserted_id))

    def process_item(self, item, spider):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.db[self.collection_name].insert_one(dict(item)))
        return


class SiteCrawlerPipeline:
    def process_item(self, item, spider):
        item['paragraph_text'] = list(map(
            lambda line: line.rstrip('\r'), item.get('paragraph_text')))
        return item
