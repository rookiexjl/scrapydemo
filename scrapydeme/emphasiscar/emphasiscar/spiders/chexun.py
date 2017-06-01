# -*- coding: utf-8 -*-
import scrapy


class ChexunSpider(scrapy.Spider):
    name = "chexun"
    allowed_domains = ["http://m.chexun.com/"]
    start_urls = ['http://http://m.chexun.com//']

    def parse(self, response):
        pass
