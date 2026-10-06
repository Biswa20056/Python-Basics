fileobj = open('/Users/biswajit/Desktop/All/Python2026/Advance_Python/read.txt','r',encoding='utf-8')
#pribnt(fileobj.read()) this will return every thing from that objest
print(fileobj)
print(fileobj.tell())
print(fileobj.read(5))
print(fileobj.read(10)) # this will only return the 1st character from that object
print(fileobj.tell())
print(fileobj.read()) # this will only return the 16th character from that object

'''
do not use fileobj.read()
and fileobj.read(integer) at a time 
the second one will return only that much from the txt file
here in the above example first line will give from first to 5 then the next line will give from 6th character'''

file2 = open('/Users/biswajit/Desktop/All/Python2026/Advance_Python/read2.txt','r')
print(file2)
print(file2.tell())
file2.seek(6)
print(file2.tell())
