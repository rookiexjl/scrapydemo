# coding=utf-8
from scrapy import Request
from scrapy import Spider
from car_scrapy.items import CarScrapyItem


class XiaoFeiCheSpider(Spider):
    name = "315che"
    start_urls = [
        'http://auto.m.315che.com/'
    ]

    def parse(self, response):
        href_list = set(response.xpath('//*[@id="wrapper1"]/main/main/div[3]/div/div[2]/ul/li/a/@href').extract())
        for href in href_list:
            yield Request(href, callback=self.parse1)

    def parse1(self, response):
        namelist = response.xpath('//*[@id="wrapper1"]/main/section/div/ul/li/a/div/h5/text()').extract()
        brand = response.xpath('//*[@id="wrapper1"]/main/section/div[1]/ul/li/h2/a/text()').extract()
        type = response.xpath('//*[@id="wrapper1"]/main/section/p/text()').extract()
        url_list = response.xpath('//*[@id="wrapper1"]/main/section/div/ul/li/a/@href').extract()
        for i in range(len(namelist)):
            item = CarScrapyItem()
            item['brand'] = brand[0]
            item['type'] = type[0]
            item['url'] = url_list[i+1].split('//')[1]
            item['name'] = namelist[i].replace('&nbsp', '')
            yield item
