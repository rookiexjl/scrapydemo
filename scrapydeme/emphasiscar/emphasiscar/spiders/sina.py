# -*- coding: utf-8 -*-
import scrapy


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["http://auto.sina.cn"]
    start_urls = ['http://http://auto.sina.cn/']

    def parse(self, response):
        pass
