import scrapy
from mycrawler.items import BooksItem

class Yes24Spider(scrapy.Spider):
    name = "book-list"

    def start_requests(self):
        urls = [
            'http://www.yes24.com/24/category/bestseller',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  

    def parse(self, response):
        try:
            book_list = response.css('ol > li')
            product = BooksItem()

            for book in book_list:

                product['title'] = book.css('p:nth-child(3) > a::text').get()
                product['author'] = book.css('.aupu > a:nth-child(1)::text').get()
                product['publisher'] = book.css('.aupu > a:nth-child(2)::text').get()
                product['price']= book.css('.price > strong::text').get()
                product['description'] = book.css('.copy > a::text').get()

                # print('제목: %s, 저자: %s, 출판사: %s, 가격: %s, 설명: %s' %(title, author, publisher, price, description))
                yield product
                
        except Exception as e:
            print('e: ', e)