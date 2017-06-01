# coding=utf-8
from scrapy import Request
from scrapy import Spider

from car_scrapy.items import CarScrapyItem


class AutohomeSpider(Spider):
    name = "autohome.new"
    start_urls = [
        "http://www.autohome.com.cn/grade/carhtml/A.html",
        "http://www.autohome.com.cn/grade/carhtml/B.html",
        "http://www.autohome.com.cn/grade/carhtml/C.html",
        "http://www.autohome.com.cn/grade/carhtml/D.html",
        "http://www.autohome.com.cn/grade/carhtml/E.html",
        "http://www.autohome.com.cn/grade/carhtml/F.html",
        "http://www.autohome.com.cn/grade/carhtml/G.html",
        "http://www.autohome.com.cn/grade/carhtml/H.html",
        "http://www.autohome.com.cn/grade/carhtml/I.html",
        "http://www.autohome.com.cn/grade/carhtml/J.html",
        "http://www.autohome.com.cn/grade/carhtml/K.html",
        "http://www.autohome.com.cn/grade/carhtml/L.html",
        "http://www.autohome.com.cn/grade/carhtml/M.html",
        "http://www.autohome.com.cn/grade/carhtml/N.html",
        "http://www.autohome.com.cn/grade/carhtml/O.html",
        "http://www.autohome.com.cn/grade/carhtml/P.html",
        "http://www.autohome.com.cn/grade/carhtml/Q.html",
        "http://www.autohome.com.cn/grade/carhtml/R.html",
        "http://www.autohome.com.cn/grade/carhtml/S.html",
        "http://www.autohome.com.cn/grade/carhtml/T.html",
        "http://www.autohome.com.cn/grade/carhtml/U.html",
        "http://www.autohome.com.cn/grade/carhtml/V.html",
        "http://www.autohome.com.cn/grade/carhtml/W.html",
        "http://www.autohome.com.cn/grade/carhtml/X.html",
        "http://www.autohome.com.cn/grade/carhtml/Y.html",
        "http://www.autohome.com.cn/grade/carhtml/Z.html",
    ]

    def parse(self, response):
        xPath = u'//ul[@class="rank-list-ul"]/li/h4/a/@href'
        resList1 = response.xpath(xPath).extract()

        for i in range(1, len(resList1) + 1):
            carURL = resList1[i - 1]
            yield Request(carURL,  callback=self.parse_detail)

    def parse_detail(self,response):
        item = CarScrapyItem()
        xPath = u'//div[@class="subnav-title-name"]/a/text()'
        resList1 = response.xpath(xPath).extract()
        item['brand'] = resList1[0]
        xPath = u'//div[@class="subnav-title-name"]/a/h1/text()'
        name = response.xpath(xPath).extract()

        if len(name)>0:
            item['name'] = name[0]
        else:
            xPath = u'//div[@class="subnav-title-name"]/a/text()'
            name = response.xpath(xPath).extract()
            name=name[0].split('-')
            item['name'] = name[1]

        xPath = u'//div[@class="subnav-title-name"]/a/@href'
        url = response.xpath(xPath).extract()
        URL = 'm.autohome.com.cn' + url[0]
        item['url'] = URL
        item['type'] = None
        yield item
