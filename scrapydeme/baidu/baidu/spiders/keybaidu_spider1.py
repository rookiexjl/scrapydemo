# coding=utf-8
from scrapy import Request
from scrapy import Spider

from baidu.items import BaiduItem


class KacheSpider(Spider):
    name = "baidukey"
    start_urls = [
        'https://m.baidu.com/s?word=企业歌曲',
        'https://m.baidu.com/s?word=广告歌曲',
        'https://m.baidu.com/s?word=商会歌曲',
        'https://m.baidu.com/s?word=协会歌曲',
        'https://m.baidu.com/s?word=校歌',
        'https://m.baidu.com/s?word=活动主题曲',
        'https://m.baidu.com/s?word=城市歌曲',
        'https://m.baidu.com/s?word=旅游歌曲',
        'https://m.baidu.com/s?word=原创音乐',
        'https://m.baidu.com/s?word=地方形象歌曲',
        'https://m.baidu.com/s?word=村歌镇歌',
        'https://m.baidu.com/s?word=集团歌曲',
        'https://m.baidu.com/s?word=司歌创作',
        'https://m.baidu.com/s?word=歌曲制作公司',
        'https://m.baidu.com/s?word=励志歌曲',
        'https://m.baidu.com/s?word=企业歌曲制作',
        'https://m.baidu.com/s?word=企业歌曲创作',
        'https://m.baidu.com/s?word=厂歌制作',
        'https://m.baidu.com/s?word=校歌制作',
        'https://m.baidu.com/s?word=歌曲定制',
        'https://m.baidu.com/s?word=餐饮行业歌曲',
        'https://m.baidu.com/s?word=美发行业歌曲',
        'https://m.baidu.com/s?word=食品行业歌曲',
        'https://m.baidu.com/s?word=影视主题曲',
        'https://m.baidu.com/s?word=歌曲MV',
        'https://m.baidu.com/s?word=企业歌曲制作公司',
        'https://m.baidu.com/s?word=歌曲创作公司',
    ]

    def parse(self, response):
        xPath = u'//*[@id="results"]/div/div/div/div/a[1]/@href'
        resList1 = response.xpath(xPath).extract()
        xPath = u'//*[@id="kw"]/text()'
        name = response.xpath(xPath).extract()[0]
        for url in resList1:
            yield Request(url, callback = self.parse1, meta={'name': name})
        print "************************************"
        xPath = u'//*[@id="page-controller"]/div/a/@href'
        resList1 = response.xpath(xPath).extract()
        if len(resList1) > 0:
            yield Request(resList1[0], callback=self.parse)

    def parse1(self, response):
        item = BaiduItem()
        name = response.meta['name']
        item['url'] = response.url
        print name
        item['name'] = name
        yield item
