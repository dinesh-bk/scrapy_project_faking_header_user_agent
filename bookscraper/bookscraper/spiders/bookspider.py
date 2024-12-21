import scrapy
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    # Spider name
    name = "bookspider"
    # List of allowed domains
    allowed_domains = ["books.toscrape.com"]
    # Starting URL
    start_urls = ["https://books.toscrape.com"]

    # To overwrite feeds
    custom_settings = {
        'FEEDS': {
            'booksdata.json': {'format': 'json', 'overwrite': True},
        }
    }

    def parse(self, response):
        # Let's grab all the books on the page
        books = response.css("article.product_pod")

        # Let's iterate over all the books
        for book in books:
            # Let's grab the book url 
            relative_url = book.css('h3 a ::attr(href)').get()

            # Some page have catalogue/ in the url, so we need to check if it is already in the url
            if "catalogue/" in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url

            yield response.follow(book_url, callback=self.parse_book_page)
        
        
        # After completing the current page, we need to check if there is a next page
        # If there is a next page, we will got to the page and call the parse function again

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page

            yield response.follow(next_page_url, callback=self.parse)
        

    def parse_book_page(self, response):

        # Let's grab the table rows
        table_rows = response.css("table tr")

        # Let's create a BookItem object
        book_item = BookItem()

        book_item['url']= response.url,
        book_item['title']= response.css(".product_main h1::text").get(),
        book_item['upc'] = table_rows[0].css("td::text").get(),
        book_item['product_type']= table_rows[1].css("td::text").get(),
        book_item['price_excl_tax']= table_rows[2].css("td::text").get(),
        book_item['price_incl_tax']= table_rows[3].css("td::text").get(),
        book_item['tax']= table_rows[4].css("td::text").get(),
        book_item['availability']= table_rows[5].css("td::text").get(),
        book_item['num_reviews']= table_rows[6].css("td::text").get(),
        book_item['stars']= response.css("p.star-rating").attrib['class'],
        book_item['category']= response.xpath('//ul[@class="breadcrumb"]/li[@class="active"]/preceding-sibling::li[1]/a/text()').get(),
        book_item['description']= response.xpath("//div[@id='product_description']/following-sibling::p[1]/text()").get(),
        book_item['price']= response.css(".price_color::text").get(),
        
        yield book_item

            

