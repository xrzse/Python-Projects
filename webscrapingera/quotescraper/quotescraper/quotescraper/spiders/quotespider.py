import scrapy
from quotescraper.items import QuoteItem

class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["goodreads.com"]
    start_urls = ["https://goodreads.com/quotes"]

    def parse(self, response):
        quotes = response.css('div.quotes .quoteDetails')

        for quote in quotes:
            quote_item = QuoteItem()
            quote_item['quote'] = quote.css('.quoteText::text').get()
            quote_item['author'] = quote.css('.quoteText .authorOrTitle::text').get()
            yield quote_item

        next_page = response.css('a.next_page::attr(href)').get()
        if next_page is not None:
            next_page_url = 'https://www.goodreads.com/' + next_page
            yield response.follow(next_page_url, callback=self.parse)
