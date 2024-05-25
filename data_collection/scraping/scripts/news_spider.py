import scrapy
from datetime import datetime
from database.database_manager import DatabaseManager

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [
      
        # Add more URLs as needed
    ]

    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.db_manager = DatabaseManager()

    async def parse(self, response):
        # Extract data from the webpage using XPath or CSS selectors
        news_items = response.xpath('//div[@class="news-item"]')

        for news_item in news_items:
            # Extract relevant data from the news item
            title = news_item.xpath('./h2/a/text()').get()
            link = news_item.xpath('./h2/a/@href').get()
            date_published = news_item.xpath('./span[@class="date"]/text()').get()

            # You may need to further process the extracted data (e.g., date formatting)
            date_published = datetime.strptime(date_published, "%Y-%m-%d")

            # Insert data source and retrieve source_id
            source_name = "Example News"  # Adjust as needed
            source_url = response.url
            source_id = await self.insert_data_source(source_name, source_url, date_published)

            # Insert raw text data
            raw_text_id = self.db_manager.insert_raw_text_data(content=title, source_id=source_id, date_collected=date_published)

        # Close the database connection when finished parsing
        self.db_manager.close()

    async def insert_data_source(self, source_name, source_url, last_scraped):
        source_id = self.db_manager.insert_data_source(source_name=source_name, source_url=source_url, last_scraped=last_scraped)
        return source_id
