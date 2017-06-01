# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
from car_scrapy.items import CarScrapyItem


class CheXunSpider(Spider):
    name = "chexun"
    start_urls = [
        'http://m.chexun.com/select-car/brandlist.aspx'
    ]

    def parse(self, response):
        hreflist = set(response.xpath('//*/ul/li/a/@data-brandid').extract())
        for href in hreflist:
            url = 'http://m.chexun.com/select-car/companylist.json?brandId=' + href
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        txt1 = response.xpath('/html/body/p/text()').extract()
        try:
            for company in demjson.decode(txt1[0])["companyList"]:
                for series in company["seriesList"]:
                    item = CarScrapyItem()
                    item['brand'] = company["companyName"]
                    item['type'] = None
                    item['url'] = 'm.chexun.com/auto/' + series["english"] + '/'
                    item['name'] = series["name"]
                    yield item
        except:
            pass
