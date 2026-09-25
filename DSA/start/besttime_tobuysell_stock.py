nums = [7,2,1,5,6,4,8]
'''n = len(nums)
profit = float('-inf')
for i in range(n):
    cur_profit = 0
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            cur_profit = nums[j]-nums[i]
            profit = max(profit,cur_profit)
print(profit) '''

nums = [7,2,1,5,6,4,8]
min_price = float('inf')
max_profit = 0
n = len(nums)
for i in range(n):
    min_price = min(min_price,nums[i])
    max_profit = max(max_profit,nums[i]-min_price)
print(max_profit)