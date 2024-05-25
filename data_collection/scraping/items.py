import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    publication_date = scrapy.Field()
    content = scrapy.Field()
