# coding:utf-8
import urllib2
import sys
import random
from bs4 import BeautifulSoup
from selenium import webdriver


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class ifeng_spider():
    def __init__(self):
        self.proxies_list = []

    def judge_ip(self):
        '''Judge IP can use or not'''
        fp1 = open('ip')
        for record in fp1:
            http_url = "http://www.baidu.com/"
            https_url = "https://www.alipay.com/"
            proxy_type = 'http'
            url = http_url if proxy_type == "http" else https_url
            proxy = record.strip('\r').strip('\n')
            try:
                req = urllib2.Request(url=url)
                req.set_proxy(proxy, proxy_type)
                response = urllib2.urlopen(req, timeout=30)
            except Exception, e:
                print "Request Error:", e
            else:
                code = response.getcode()
                if 200 <= code < 300:
                    print 'Effective proxy', proxy
                    self.proxies_list.append(proxy)
                else:
                    print 'Invalide proxy', proxy
        return self.proxies_list

    def openurl_test(self, ipp, link):
        try:
            urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({"http": ipp})))
            html_content = urllib2.urlopen(link, timeout=30).read()
            return html_content
        except:
            print random.sample(self.proxies_list, 1)[0]
            self.openurl_test(random.sample(self.proxies_list, 1)[0], link)


def main():
    browser = webdriver.Firefox()
    browser.get('http://iauto.ifeng.com/index.php?c=search&a=index&wap=2')
    brand_list = []
    url_list = []
    for i in range(1, 149):
        xpath = '//*[@id="main"]/div[5]/ul[' + str(i) + ']/li[1]/a/span'
        brand = browser.find_element_by_xpath(xpath).text
        brand_list.append(brand)
        xpath1 = '//*[@id="main"]/div[5]/ul[' + str(i) + ']/li[1]/a'
        link = browser.find_element_by_xpath(xpath1).get_attribute('href')
        url_list.append(link)
    browser.quit()
    a = ifeng_spider()
    proxies_list = a.judge_ip()
    for i in range(len(brand_list)):
        html = a.openurl_test(random.sample(proxies_list, 1)[0], url_list[i])
        if html:
            pass
        else:
            continue
        soup = BeautifulSoup(html, 'lxml')
        if soup.find('span', class_='n'):
            for page in range(1, int(soup.find('span', class_='n').string.split('/')[1]) + 1):
                link = url_list[i] + '&page=' + str(page)
                html1 = a.openurl_test(random.sample(proxies_list, 1)[0], link)
                if html1:
                    pass
                else:
                    continue
                soup1 = BeautifulSoup(html1, 'lxml')
                for li in soup1.find_all('li'):
                    url = 'iauto.ifeng.com/' + li.a.get('href')
                    name = li.a.span.string
                    brand = brand_list[i].encode('utf8')
                    line = url + ',' + brand + ',' + name
                    with open('ifeng3.csv', 'a') as f:
                        f.write(line + '\n')
        else:
            for li in soup.find_all('li'):
                url = 'iauto.ifeng.com/' + li.a.get('href')
                name = li.a.span.string
                brand = brand_list[i].encode('utf8')
                line = url + ',' + brand + ',' + name
                with open('ifeng3.csv', 'a') as f:
                    f.write(line + '\n')


if __name__ == '__main__':
    main()
