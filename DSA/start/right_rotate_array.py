n = [5,-2,3,9,0,6,10,7]
n1 = len(n)
k = 1
temp = n[n1-k]
for i in range(n1-1,0,-1):
    n[i] = n[i-1]

n[k-1] = temp
print(n)

# right rotate by k place

a = [3,9,5,6,7,2]
length = len(a)
k = 7
temp = a[length-k:]# here for larger length it is getting wrong output
for i in range(length-1,k-1,-1):
    a[i] = a[i-k]
temp_len = len(temp)
for i in range(temp_len):
    a[i] = temp[i]
print(a)

# brute force
x = [3,9,5,6,7,2]
y = len(x)
k = 14
loop = k%y
for _ in range(loop):
    e = x.pop()
    x.insert(0,e)
print(x)

# better by slicing
k = [3,9,5,6,7,2,10,9]
m = len(k)
l = 5
l = m%l
k[:] = k[m-l:] + k[:m-l]
print(k)
