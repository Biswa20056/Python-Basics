n = -7789
n = abs(n)
count = 0
while n>0:
    count +=1
    n//=10
print(count)

print('--------By logarithm method')
import math
n = 7789
count = int(math.log10(n) + 1)
print(count)