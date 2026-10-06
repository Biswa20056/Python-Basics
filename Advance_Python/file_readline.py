fileobj = open('/Users/biswajit/Desktop/All/Python2026/Advance_Python/read.txt','r',encoding='utf-8')
print(fileobj)
print(fileobj.tell())
print(fileobj.readline()) 
print(fileobj.tell())
print(fileobj.readline())# this will only read the first line at a time
print(fileobj.tell())
print(fileobj.readline(6))
print(fileobj.tell())
print(fileobj.readline())
 # this will return all the remaining lines in the form of a list




