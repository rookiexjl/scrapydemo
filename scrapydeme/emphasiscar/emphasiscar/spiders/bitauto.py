# -*- coding: utf-8 -*-
import scrapy


class BitautoSpider(scrapy.Spider):
    name = "bitauto"
    allowed_domains = ["http://m.bitauto.com"]
    start_urls = ['http://http://m.bitauto.com/']

    def parse(self, response):
        pass
