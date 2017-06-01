# coding:utf-8
import re
import urllib2
from scrapy import Request
from scrapy import Spider

from fang.items import FangItem


class LoupanSpider(Spider):

    name = "tengxun"
    start_urls = [
        'http://db.house.qq.com/index.php?mod=search&act=newsearch&city=hz&showtype=2&unit=1&all=&page_no=1&mod=search&city=hz'
    ]

    def parse(self, response):
        for i in range(1, 138):
            url = 'http://db.house.qq.com/index.php?mod=search&act=newsearch&city=hz&showtype=2&unit=1&all=&page_no=' + str(i) + \
                     '&mod=search&city=hz'
            yield Request(url, callback=self.parse1)

    def parse1(self, response):
        html = html = urllib2.urlopen(response.url).read()
        a = re.findall(r'(data-hid.\\.[0-9]*)', html)
        b = []
        for i in a:
            b.append(i.split('"')[1])
        for i in b:
            url = 'http://m.db.house.qq.com/hz_' + i +'/'
            yield Request(url, callback=self.parse2)

    def parse2(self, response):
        item = FangItem()
        item['url'] = response.url
        xPath = u'//body/div[1]/div[@class="p-houseinfo v-box"]/h2/text()'
        item['name'] = response.xpath(xPath).extract()
        yield item