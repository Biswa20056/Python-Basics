# brute force approach
'''a = [1,1,2,2,2,3,3,4,4]
s = set()
n = len(a)
for idx in range(n):
    s.add(a[idx])
print(len(list(s)))'''

# optimal approach
a = [1,1,2,2,2,3,3]
i = 0
n = len(a)
for j in range(1,n):
    if a[i]!=a[j]:
        a[i+1] = a[j]
        i+=1
        
print(i+1)