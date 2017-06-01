# -*- coding: utf-8 -*-
import scrapy


class IfengSpider(scrapy.Spider):
    name = "ifeng"
    allowed_domains = ["http://i.ifeng.com/auto/autoi"]
    start_urls = ['http://http://i.ifeng.com/auto/autoi/']

    def parse(self, response):
        pass
