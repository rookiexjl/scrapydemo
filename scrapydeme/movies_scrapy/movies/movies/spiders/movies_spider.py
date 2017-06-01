# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from movies.items import MoviesItem


class MoviesSpiderSpider(scrapy.Spider):
    name = "movies"
    # allowed_domains = []
    start_urls = ['http://www.qq.com']

    # def parse(self, response):
    #     # link_list = response.xpath('//*/div/div/div/div/div/ul/li/a/@href').extract()
    #     # for i in link_list:
    #     #     url = 'http://www.dy2018.com' + i
    #     url = 'http://www.dy2018.com/i/98038.html'
    #     yield Request(url, callback=self.parse1)
    #
    # def parse1(self, response):
    #     items = MoviesItem()
    #     # items['name'] = response.xpath('//*[@class="title_all"]/h1/text()').extract()[0]
    #     items['url'] = response.xpath('//*/tbody/tr/td/a/text()').extract()[0]
    #     yield items
    def parse(self, response):
        items = MoviesItem()
        # items['name'] = response.xpath('//*[@class="title_all"]/h1/text()').extract()[0]
        items['url'] = 'ftp://y:y@dygod18.com'
        yield items
