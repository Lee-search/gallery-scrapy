# DCinside Gallery Scrapy

디시인사이드 갤러리 크롤러.
오픈소스 크롤링 프레임워크 Scrapy를 사용하였습니다.

# Require

1. [Python][Py_link]
2. [Scrapy][Sc_link]

[Py_link]: https://www.python.org/
[Sc_link]: https://scrapy.org/

# Usage

```
scrapy crawl gall-list
```
# Details

## mycrawler/spiders/dcinside_spider.py

* Main Crawler
  크롤러가 정의된 부분

## mycrawler/spiders/others

* Sub or Testing Crawler
  연습용으로 만든 크롤러들로 무시하셔도 됩니다.

## mycrawler/items.py

* Item List
  아이템의 형식에 크롤링 데이터가 짜맞추어집니다.

## mycrawler/pipelines.py

* Pipeline List
  크롤링 된 데이터가 로컬 저장소에 저장되는 경로를 지정해줍니다.

### mycrawler/settings.py

* Configurations
  크롤러의 설정이 저장됩니다.
  (주석처리된 부분 이외의 영역에 유의)
