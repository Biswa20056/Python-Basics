a = [1,2,3,4,5,6,7]
k = 3
temp = a[0:k]
n = len(a)
for i in range(k,n):
    a[i-k]=a[i]
j = 0
for i in range(n-k,n):
    a[i] = temp[j]
    j+=1
print(a)

