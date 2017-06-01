fp1 = open('newdata')
for i in fp1:
    if i.find('http://') != -1:
        with open('newdata1', 'a') as f:
            f.write(i.split('http://')[1])
    else:
        with open('newdata1', 'a') as f:
            f.write(i)
