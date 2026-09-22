'''a = [1,0,2,3,2,0,0,4,5,1]
temp = []
n = len(a)
for idx in range(n):
    if a[idx]!=0:
        temp.append(a[idx])
n1 = len(temp)
for idx in range(n1):
    a[idx] = temp[idx]
nonzero = len(temp)
for idx in range(nonzero,n):
    a[idx]=0
print(a)'''
# the above code is brute force method
a = [1,0,2,3,2,0,0,4,5,1]
j = -1
n = len(a)
for idx in range(n):
    if a[idx]==0:
        j = idx
        break
for i in range(j+1,n):
    if a[i]!=0:
        a[i],a[j] = a[j],a[i]
        j+=1
        
print(a)
