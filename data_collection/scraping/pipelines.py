class NewsPipeline:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    @classmethod
    def from_crawler(cls, crawler):
        return cls(db_manager=crawler.spider.db_manager)

    async def process_item(self, item, spider):
        # Insert item into database
        if spider.name == 'news_spider':
            title = item.get('title')
            url = item.get('url')
            publication_date = item.get('publication_date')
            content = item.get('content')
            await self.db_manager.insert_news_data(title, url, publication_date, content)
        return item
