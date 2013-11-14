# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'
DEPTH_LIMIT = 2
ITEM_PIPELINES = ['dirbot.pipelines.FilterWordsPipeline']
