'''nums = [5,10,-3,-1,-10,6]
n = len(nums)
a = []
b = []
for i in range(n):
    if nums[i]>=0:
        a.append(nums[i])
    elif nums[i]<0:
        b.append(nums[i])
i = 0
j = 0
res = []
while i<len(a) and j<len(b):
    res.append(a[i])
    i+=1
    res.append(b[j])
    j+=1
print(res)'''

# optimal solution by two pointer
nums = [5,10,-3,-1,-10,6]
n = len(nums)
res = [0]*n
i = 0
j = 1
for idx in range(n):
    if nums[idx]>=0:
        res[i] = nums[idx]
        i+=2
    else:
        res[j] = nums[idx]
        j+=2    
print(res)

