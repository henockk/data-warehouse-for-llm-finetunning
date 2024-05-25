BOT_NAME = 'scraping'

SPIDER_MODULES = ['scraping.spiders']
NEWSPIDER_MODULE = 'scraping.spiders'

ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'scraping.pipelines.NewsPipeline': 300,
}

# Custom middleware
DOWNLOADER_MIDDLEWARES = {
    'scraping.middlewares.CustomDownloaderMiddleware': 543,
}
