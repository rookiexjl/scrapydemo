# -*- coding: utf-8 -*-
import scrapy


class PcautoSpider(scrapy.Spider):
    name = "pcauto"
    allowed_domains = ["http://m.pcauto.com.cn/"]
    start_urls = ['http://http://m.pcauto.com.cn//']

    def parse(self, response):
        pass
