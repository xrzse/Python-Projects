import scrapy

class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["goodreads.com"]
    start_urls = ["https://goodreads.com/quotes"]

    def parse(self, response):
        quotes = response.css('div.quotes .quoteDetails')
        len(quotes)

        for quote in quotes:
            yield {
                'quote' : quote.css('.quoteText::text').get()
            }
