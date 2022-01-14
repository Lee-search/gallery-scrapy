# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#from itemadapter import ItemAdapter
#from scrapy.exporters import JsonItemExporter
#
#class MycrawlerPipeline:
#    def process_item(self, item, spider):
#        with open('books.json', 'wb') as f:
#            exporter = JsonItemExporter(f, encoding='utf-8')
#            exporter.export_item(item)
#        return item

from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter, CsvItemExporter

import time

now = time.localtime()
dates = time.strftime('%Y%m%d', now)

class JsonWriterPipeline:

    def __init__(self):
        self.file = open("output/scrapy_list_" + dates + ".json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
 
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
 
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class CsvWriterPipeline:

    def __init__(self):
        self.file = open("output/scrapy_list_" + dates + ".csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

