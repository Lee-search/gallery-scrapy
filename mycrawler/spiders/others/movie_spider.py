import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"

    def start_requests(self):
        urls = [
            'https://movie.naver.com/movie/running/current.naver?order=reserve',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            item = {}
            movie_sels = response.css('ul.lst_detail_t1 > li')

            for movie_sel in movie_sels:

                item['title'] = movie_sel.css('.tit > a::text').get()
                item['age_limit'] = movie_sel.css('.tit > span::text').get()
                item['rating'] = movie_sel.css('.star_t1 > a > span.num::text').get()
                item['rating_count'] = movie_sel.css(".star_t1 > a > span.num2 > em::text").get()

                #print('제목: %s, 연령제한: %s, 평점: %s, 참여자 수: %s' %(item['title'], item['age_limit'], item['rating'], item['rating_count'])
                yield item
        except Exception as e:
            print('e: ', e)
