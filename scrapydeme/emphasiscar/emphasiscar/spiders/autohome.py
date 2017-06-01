# -*- coding: utf-8 -*-
import scrapy


class AutohomeSpider(scrapy.Spider):
    name = "autohome"
    allowed_domains = ["http://m.autohome.com.cn/"]
    start_urls = ['http://http://m.autohome.com.cn//']

    def parse(self, response):
        pass
