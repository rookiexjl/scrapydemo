# -*- coding: utf-8 -*-
import scrapy


class HaomaicheSpider(scrapy.Spider):
    name = "haomaiche"
    allowed_domains = ["http://m.haomaiche.com"]
    start_urls = ['http://http://m.haomaiche.com/']

    def parse(self, response):
        pass
