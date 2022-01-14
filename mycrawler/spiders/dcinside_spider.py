import scrapy
from mycrawler.items import PostItem

class GallerySpider(scrapy.Spider):
    name = "gall-list"

    def start_requests(self):
        urls = []
        TOTAL_PAGE = 10
        
        for pages in range(0, TOTAL_PAGE):
            urls.append('https://gall.dcinside.com/mgallery/board/lists/?id=stockus&page=' + str(pages+1))  # 미주갤
            #urls.append('https://gall.dcinside.com/mgallery/board/lists/?id=tenbagger&page=' + str(pages+1))   # 해주갤
        #print(urls)

        for url in urls: 
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            crawlPage = response.css('tbody > tr')
            crawlPost = PostItem() 
            
            for post in crawlPage:

                postTitle = post.css('td.gall_tit.ub-word > a::text').get()
                
                if postTitle is not None:
                    crawlPost['title'] = postTitle
                    crawlPost['author'] = post.css('td.gall_writer.ub-writer > span.nickname > em::text').get() 
                    crawlPost['dates'] =  post.css('td.gall_date::attr("title")').get() 
                    crawlPost['views'] = post.css('td.gall_count::text').get()

                    #print('제목: %s, 글쓴이: %s, IP: %s, 날짜: %s, 조회수: %s' %(title, author, dates, views))
                    yield crawlPost
                    
                else:
                    yield
                
        except Exception as e:
            print('e: ', e)