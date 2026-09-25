nums = [1,1,0,1,0,1,1,1,1,1,0,1,1]
n = len(nums)
i = 0
count = 0
max_count = 0
while i<n:
    if nums[i]==1:
        count+=1
        if count>max_count:
            max_count = max(max_count,count)
    else:
        count = 0
    i+=1
print(max_count)
