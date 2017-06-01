# coding:utf-8
file_dir = 'findKeyString'
a = '重构日本'
b = ['日本']
filters = ['招聘', '诚聘', '社招']
contents = [
    '独自等待安全团队诚聘, http://www.jb51.net/',
    '独自等待安全团队招聘, http://www.jb51.net/',
    '独自等待安全团队社招, http://www.jb51.net/',
    '独自等待信息安全博客, http://www.jb51.net/',
]

for content in contents:
    if any(keyword in content for keyword in filters): continue
    print content