import scrapy

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com'] #prevents spider from wandering off into other websites
    start_urls = ['http://books.toscrape.com/'] #Can have multiple websites

    def parse(self, response):
        books = response.css('article.product_pod') #gets all the html for article and class of product_pod
        for book in books:
            yield{
                'name' : book.css('h3 a::text').get(),
                'price' : book.css('div.product_price p.price_color::text').get(),
                'url' : book.css('h3 a').attrib['href'],
            } #function gets the name,price,url of each book in the html page it is currently on.

        next_page = response.css('li.next a::attr(href)').get() #identifying next page url 

        if next_page is not None: #this function is what loops through the entire websites pages.

            #the url of the next page button switches for a few pages so dealt with that with an if statement.
            if 'catalogue/' in next_page:
                next_page_url = 'http://books.toscrape.com/' + next_page
            else:
                next_page_url = 'http://books.toscrape.com/catalogue/' + next_page

                #After it goes to next page it loops back to the original function to get all book names
            yield response.follow(next_page_url, callback= self.parse)
