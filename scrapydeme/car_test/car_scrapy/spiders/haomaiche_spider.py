# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
from car_scrapy.items import CarScrapyItem


class HaoMaiCheSpider(Spider):
    name = "haomaiche"
    fp1 = open('haomaiche.txt', 'r')
    list = fp1.readline()[2:-2].split('},{')
    start_urls = []
    for i in list:
        start_urls.append("http://api.haomaiche.com/ware/car/330100/" + i.split(':')[-1].strip('"')
                          + "/car-type?carBrandId=" + i.split(':')[-1].strip('"')
                          + "&cityCode=330100&source=102")

    def parse(self, response):
        json_data = response.xpath('/html/body/p/text()').extract()
        try:
            for brandName in demjson.decode(json_data[0])['data']['carTypeList']:
                for typelist in brandName['typeList']:
                    item = CarScrapyItem()
                    item['brand'] = brandName['brandName']
                    item['url'] = 'm.haomaiche.com/hz/car_parity_detail/' + typelist['typeId']
                    item['name'] = typelist['typeName']
                    item['type'] = None
                    yield item
        except:
            pass
