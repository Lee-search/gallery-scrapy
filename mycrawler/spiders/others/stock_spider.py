import scrapy

class Stock(scrapy.Item):
    name = scrapy.Field()

class StockSpider(scrapy.Spider):
    name = "stock-list"

    def start_requests(self):
        urls = ["https://www.waytoliah.com/1505?category=969385"]

        for url in urls: 
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            crawlPage = response.css('tbody')
            stockData = Stock()
            
            for data in crawlPage:
                stockData["name"] = data.css('tr > td > span > span > span > b::text').get()
                yield stockData
 
        except Exception as e:
            print('e: ', e)