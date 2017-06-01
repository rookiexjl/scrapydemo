# -*- coding: utf-8 -*-
import scrapy


class QqSpider(scrapy.Spider):
    name = "qq"
    allowed_domains = ["http://w.auto.qq.com"]
    start_urls = ['http://http://w.auto.qq.com/']

    def parse(self, response):
        pass
