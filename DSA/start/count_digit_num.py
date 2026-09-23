n = 5873
dup = n
count = 0
while n>0:
    rem = n%10
    count+=1
    n//=10
print(count)

# by log 
from math import *
no = log10(5873)
print(int(no)+1)