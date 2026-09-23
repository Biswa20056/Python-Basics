a = [1,1,0,1,1,1,0,1,1]
n = len(a)
max = 0
count = 0
for i in range(n):
    if a[i]==1:
        count+=1
        if count >= max:
            max = count
    else:
        if a[i]==0:
            count = 0
print(max) 