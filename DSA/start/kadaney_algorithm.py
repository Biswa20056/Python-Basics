nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
current = 0
max_sum = float('-inf')
for i in range(n):
    current += nums[i]
    max_sum = max(current,max_sum)
    if current<0:
        current = 0
print(max_sum)