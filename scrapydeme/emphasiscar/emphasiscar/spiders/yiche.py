# -*- coding: utf-8 -*-
import scrapy


class YicheSpider(scrapy.Spider):
    name = "yiche"
    allowed_domains = ["http://m.yiche.com"]
    start_urls = ['http://http://m.yiche.com/']

    def parse(self, response):
        pass
