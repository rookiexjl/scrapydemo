#  coding:utf-8
# from pyquery import PyQuery as pq
#
# p = pq('<p id="hello" class="hello1"></p>')
# print p.append('check out<a href="http://reddit.com/r/python"><span>reddit</span></a>')
# print p.prepend('Oh yes!')
# d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
# p.prepend_to(d('#test'))
# print p
# print d
# d.empty()
# print d


# from pyquery import PyQuery as pq
# doc = pq(filename='hello.html')
# lis = doc('li')
# for li in lis.items():
#     print li.html()
#
# print lis.each(lambda e: e)


from pyquery import PyQuery as pq

#print pq('http://cuiqingcai.com', headers={'user-agent': 'pyquery'})
print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True)
