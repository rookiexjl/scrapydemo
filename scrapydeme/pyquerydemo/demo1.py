# coding:utf-8
# from pyquery import PyQuery as pq
#
# doc = pq(filename='hello.html')
# print doc.html()
# print type(doc)
# li = doc('li')
# print type(li)
# print li.text()


# from pyquery import PyQuery as pq
# p = pq('<p id="hello" class="hello1"></p>')('p')
# print p.attr('id')
# print p.attr('id', 'plop')
# print p
# print p.attr('id', 'hello')
# print p


from pyquery import PyQuery as pq
p = pq('<p id="hello" class="hello1"></p>')('p')
print p.add_class('beauty')
print p.remove_class('hello1')
print p.css('font-size', '16px')
print p.css({'background-color':'yellow'})

