# coding:utf-8
# import urllib2
# from bs4 import BeautifulSoup
# response = urllib2.urlopen('http://iauto.ifeng.com/index.php?c=search&a=list&brand=10004&wap=2')
# html = response.read()
# soup = BeautifulSoup(html, 'lxml')
# if soup.find('span', class_='n'):
#     print '1'
# else:
#    print '2'
# import random
# from bs4 import BeautifulSoup
# list = ['sad','dasd','dsad']
# print random.sample(list, 1)
# a = 'aa'
# #print a
# if a:
#     pass
# else:
#     a = ''
# print a
# soup = BeautifulSoup(a, 'lxml')
# print soup.find('span', class_='n')
# if soup.find('span', class_='n'):
#     print '1'
# else:
#     print '2'
lines = 'iauto.ifeng.com/index.php?c=serial&a=index&sid=10541&wap=2'
if lines.find('iauto.ifeng') != -1:
    a = lines.split('/')[0]
    b = lines.split('&')[2]
    lines = a + ' ' + b
print lines