# brute force method
a = [1,2,3,4,5]
n = len(a)
i = 0
j = n-1
while i<j:
    a[i],a[j] = a[j],a[i]
    i+=1
    j-=1
print(a)
