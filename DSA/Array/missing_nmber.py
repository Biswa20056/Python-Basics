'''a = [1,2,4,5]
for i in range(1,len(a)):
    flag = 0
    for j in range(0,len(a)-1):
        if a[j]==i:
            flag = 1
            break
    if flag==0:
        print(i)'''
# the above approach is brute force
'''a = [1,2,4,5]
n = 5
hash_arr = [0]*6
for i in range(0,n-1):
    hash_arr[a[i]]=1
for i in range(1,n):
    if hash_arr[i]==0:
        print(i)'''
# the second one is better approach
'''a = [1,2,4,5]
n = 5
sum1= n*(n+1)//2
sum2 = 0
for num in a:
    sum2+=num
missing = sum1 - sum2
print(missing)
'''
a = [1,2,4,5]
n = 5
xor1 = 0
xor2 = 0
for i in range(0,n-1):
    xor2 = xor2^a[i]
    xor1 = xor1 ^(i+1)
xor1 = xor1 ^ n
print(xor1 ^ xor2)










# this one is optimal approach