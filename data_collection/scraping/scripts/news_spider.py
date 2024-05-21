import scrapy

class AmharicNewsSpider(scrapy.Spider):
    name = "amharic_news"
    start_urls = [

    ]

    def parse(self, response):
        for article in response.css('div.article'):
            yield {
                'title': article.css('h2.title::text').get(),
                'content': article.css('div.content::text').get(),
                'date': article.css('span.date::text').get(),
                'source': response.url
            }
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
