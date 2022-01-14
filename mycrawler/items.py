# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PostItem(scrapy.Item):
    title = scrapy.Field()  # 제목
    author = scrapy.Field() # 글쓴이
    dates = scrapy.Field()  # 날짜
    views = scrapy.Field()  # 조회수
    pass

class BooksItem(scrapy.Item):
    title = scrapy.Field()          # 제목
    author = scrapy.Field()         # 글쓴이
    publisher = scrapy.Field()      # 출판사
    price = scrapy.Field()          # 가격
    description = scrapy.Field()    # 설명
    pass