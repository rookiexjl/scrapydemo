# -*- coding: utf-8 -*-
import scrapy


class CheshiSpider(scrapy.Spider):
    name = "cheshi"
    allowed_domains = ["http://a.cheshi.com/"]
    start_urls = ['http://http://a.cheshi.com//']

    def parse(self, response):
        pass
