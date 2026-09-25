'''nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)
i = 0
for idx in range(n):
    if nums[idx]==0:
        i = idx
        break
for j in range(i+1,n):
    if nums[j]!=0:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j+=1
    else:
        if nums[j]==0:
            j+=1
print(nums)

'''
# Approach 2
a = [1,0,2,4,3,0,0,3,5,1]
n = len(a)
temp = []
for i in range(n):
    if a[i]!=0:
        temp.append(a[i])
for i in range(len(temp)):
    a[i] = temp[i]
for i in range(len(temp), n):
    a[i] = 0
print(a)


# method 3
num = [1,2,0,4,3,2,0,0,5,6,0]
n = len(num)
if n==1: # edge case
    print(num)
i = 0
while i<n:
    if num[i]==0:
        break
    i+=1
if i == n:# edge case
    print(n)
j = i+1
while  j<n:
    if num[j]!=0:
        num[i],num[j] = num[j],num[i]
        i+=1
    j+=1
print(num)