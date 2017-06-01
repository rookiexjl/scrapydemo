# coding:utf8
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re


class MzituScrapyPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        """
        :param request: 每一个图片下载管道请求
        :param response: 
        :param info: 
        :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
        :return: 每套图的分类目录
        """
        item = request.meta['item']
        folder = item['name']
        folder_strip = folder.replace(' ', '')
        image_guid = request.url.split('/')[-1]
        return u'full/%s/%s' % (folder_strip, image_guid)
        # item = request.meta['item']
        # folder = item['name']
        # folder_strip = strip(folder)
        # print '-------------------------------'
        # print folder_strip
        # print request.url
        # image_guid = request.url.split('/')[-1]
        # print 'image_guid:' + image_guid
        # print '***************************************'
        # filename = u'full/{0}/{1}'.format(folder_strip, image_guid)
        # return filename

    def get_media_requests(self, item, info):
        """
        :param item: spider.py中返回的item
        :param info: 
        :return: 
        """
        for img_url in item['image_urls']:
            yield Request(img_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    # def process_item(self, item, spider):
    #     return item


# def strip(path):
#     """
#     :param path: 需要清洗的文件夹名字
#     :return: 清洗掉Windows系统非法文件夹名字的字符串
#     """
#     path = re.sub(r'[?\\*|"<>:/]', '', str(path))
#     path = path.replace(' ', '')
#     return path

# if __name__ == "__main__":
#     a = '又大又爽滑 性感'
#     print(strip(a))