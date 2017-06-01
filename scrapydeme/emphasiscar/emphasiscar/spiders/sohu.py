# -*- coding: utf-8 -*-
import scrapy


class SohuSpider(scrapy.Spider):
    name = "sohu"
    allowed_domains = ["http://m.sohu.com"]
    start_urls = ['http://http://m.sohu.com/']

    def parse(self, response):
        pass
