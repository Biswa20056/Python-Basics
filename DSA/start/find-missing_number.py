a = [1,0,3,4]
res = 0
for val in a:
    res+=val
total = len(a)*(len(a)+1)//2
print(total-res)