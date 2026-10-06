file = open('/Users/biswajit/Desktop/All/Python2026/Advance_Python/write_access_mode.py/sample2.txt','w')
print(file)
file.write('abcd\n')
file.write('hello')
print(file.tell())
file.write('python\nDSA')
file.close() # this works for saving in the text file
