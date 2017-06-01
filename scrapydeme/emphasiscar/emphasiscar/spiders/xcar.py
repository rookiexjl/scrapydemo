# -*- coding: utf-8 -*-
import scrapy


class XcarSpider(scrapy.Spider):
    name = "xcar"
    allowed_domains = ["http://a.xcar.com.cn/"]
    start_urls = ['http://http://a.xcar.com.cn//']

    def parse(self, response):
        pass
