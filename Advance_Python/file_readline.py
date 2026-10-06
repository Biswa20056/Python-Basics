fileobj = open('/Users/biswajit/Desktop/All/Python2026/Advance_Python/read.txt','r',encoding='utf-8')
print(fileobj)
print(fileobj.readline()) # this will only read the first line at a time
print(fileobj.readlines(10))
 # this will return all the remaining lines in the form of a list
