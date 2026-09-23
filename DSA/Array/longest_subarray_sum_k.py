a = [1,2,3,1,1,1,1,4,2,3]
n = len(a)
sum = 0
len = 0
k = 3
for i in range(n):
    sum+=a[i]
    if(sum==k):
        len = max(len,i+1)

            


    
