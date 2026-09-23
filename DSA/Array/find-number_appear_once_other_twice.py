# brute force approach
'''a = [1,1,2,3,3,4,4]
n = len(a)
for i in range(n):
    num = a[i]
    count = 0
    for j in range(n):
        if num==a[j]:
            count+=1
    if count==1:
        print(num)'''
# better solution by hashing
'''a = [1, 1, 2, 3, 3, 4, 4]

result = list(map(lambda x: x if a.count(x) == 1 else None, a))

print([x for x in result if x is not None])



# simple
a = [1, 1, 2, 3, 3, 4, 4]

print([x for x in a if a.count(x) == 1])'''

# by xor 
a = [1,1,2,3,3,4,4]
xor = 0
for i in range(len(a)):
    xor = xor^ (a[i])
print(xor)