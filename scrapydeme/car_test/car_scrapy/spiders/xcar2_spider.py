# coding=utf-8
from scrapy import Request
from scrapy import Spider
import demjson
from car_scrapy.items import CarScrapyItem


class XCar2Spider(Spider):
    name = "xcar2"
    start_urls = [
        'http://a.xcar.com.cn/brand/',
    ]

    def parse(self, response):
        idlist = response.xpath('/html/body/div/div/div/div/ul/li/a/@data-pbid').extract()
        for pbid in idlist:
            url = 'http://a.xcar.com.cn/carsel/pserise?pbid=' + pbid + '&xst=2'
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        txt1 = response.xpath('/html/body/p/text()').extract()
        for data in demjson.decode(txt1[0].encode("utf-8"))["data"]:
            for pslist in data["pslist"]:
                item = CarScrapyItem()
                item['type'] = data["bname"]
                item['brand'] = pslist["pbname"]
                item['url'] = 'a.xcar.com.cn/' + str(pslist["pserid"]) + '/'
                item['name'] = pslist["psname"]
                yield item
