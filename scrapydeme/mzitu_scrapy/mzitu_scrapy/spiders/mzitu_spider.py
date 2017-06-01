# coding:utf8

from scrapy import Request
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from mzitu_scrapy.items import MzituScrapyItem


class mzitu_Spider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    # start_urls = ['http://www.mzitu.com/']
    img_urls = []
    start_urls = ['http://www.mzitu.com/']
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',),
                           deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MzituScrapyItem()
        # max_num为页面最后一张图片的位置
        max_num = response.xpath('//*/div[@class="pagenavi"]/a[last()-1]/span/text()').extract()
        item['name'] = response.xpath("./*//div[@class='main']/div[1]/h2/text()").extract_first(default="N/A")
        img_url = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
        for i in range(1, int(max_num[0])):
            img = img_url[0].split('.jpg')[0][:-2]+str(i).zfill(2) + '.jpg'
            self.img_urls.append(img)
        item['image_urls'] = self.img_urls
        yield item

    def img_url(self, response, ):
        img_urls = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
        for img_url in img_urls:
            self.img_urls.append(img_url)








    #url = 'http://www.mzitu.com/page/2/'

    # def parse(self, response):
    #     item = MzituScrapyItem()
    #     href_list = response.xpath('//*[@id="pins"]/li/a/@href').extract()
    #     name_list = response.xpath('//*[@id="pins"]/li/span/a/text()').extract()
    #     for i in range(len(href_list)):
    #         item['name'] = name_list[i]
    #         yield Request(href_list[i], callback=self.img_url)
    #
    # #
    # def img_url(self, response):
    #     max_page = response.xpath('//*/div[@class="pagenavi"]/a[last()-1]/span/text()').extract()
    #     img_url = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
    #     for i in range(1, int(max_page)):
    #         img = img_url[0].split('.jpg')[0][:-2]+str(i).zfill(2) + '.jpg'
    #         self.img_urls.append(img)
    # def parse_item(self, response):
    #     print response.url
    #     """
    #     :param response: 下载器返回的response
    #     :return:
    #     """
    #     item = MzizuScrapyItem()
    #     # max_num为页面最后一张图片的位置
    #     max_num = response.xpath(
    #         "descendant::div[@class='main']/div[@class='content']/div[@class='pagenavi']/a[last()-1]/span/text()").extract_first(
    #         default="N/A")
    #     item['name'] = response.xpath("./*//div[@class='main']/div[1]/h2/text()").extract_first(default="N/A")
    #     for num in range(1, int(max_num)):
    #         # page_url 为每张图片所在的页面地址
    #         page_url = response.url + '/' + str(num)
    #         yield Request(page_url, callback=self.img_url)
    #     item['image_urls'] = self.img_urls
    #     yield item
    #
    # def img_url(self, response, ):
    #     """取出图片URL 并添加进self.img_urls列表中
    #     :param response:
    #     :param img_url 为每张图片的真实地址
    #     """
    #     img_urls = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
    #     for img_url in img_urls:
    #         self.img_urls.append(img_url)