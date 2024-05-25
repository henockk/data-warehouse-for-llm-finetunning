from scrapy import signals


class CustomDownloaderMiddleware:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls(db_manager=crawler.spider.db_manager)
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    async def process_response(self, request, response, spider):
        # Insert response data into database
        if spider.name == 'news_spider':
            title = response.xpath('//title/text()').get()
            url = request.url
            publication_date = response.xpath('//span[@class="publication_date"]/text()').get()
            content = response.xpath('//div[@class="content"]/text()').get()
            await self.db_manager.insert_news_data(title, url, publication_date, content)
        return response

    def spider_closed(self, spider):
        if hasattr(self.db_manager, 'connection'):
            self.db_manager.connection.close()
