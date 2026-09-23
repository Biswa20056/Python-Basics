a = [1,2,3,4,5,6,7]
k = 3
n = len(a)
temp = a[n-k:n]
for i in range(k,-1,-1):
    a[k+i] = a[i]
j = 0
for i in range(len(temp)):
    a[i] = temp[i]
    i+=1
print(a) 
