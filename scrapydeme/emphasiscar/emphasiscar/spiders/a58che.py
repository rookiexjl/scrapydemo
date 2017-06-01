# -*- coding: utf-8 -*-
import scrapy


class A58cheSpider(scrapy.Spider):
    name = "58che"
    allowed_domains = ["http://m.58che.com/"]
    start_urls = ['http://http://m.58che.com//']

    def parse(self, response):
        pass
