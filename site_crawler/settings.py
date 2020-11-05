# -*- coding: utf-8 -*-

# Scrapy settings for site_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'site_crawler'

SPIDER_MODULES = ['site_crawler.spiders']
NEWSPIDER_MODULE = 'site_crawler.spiders'

LOG_LEVEL = "WARNING"

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'site_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'site_crawler.middlewares.SiteCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'site_crawler.middlewares.SiteCrawlerDownloaderMiddleware': 543,
#}


# Configure item pipelines

ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 100,
    'site_crawler.pipelines.SiteCrawlerPipeline': 300,
    'site_crawler.pipelines.MongoPipeline': 400,
}

