# Brute Force method
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
'''max_count = 0
for i in range(n):
    num = nums[i]
    count = 1
    while num+1 in nums:
        count += 1
        num+=1
    max_count = max(max_count,count)
print(max_count)'''

# the below on eis better approach not optimal
'''nums.sort()
smallest = float('-inf')
largest = 0
count = 0
for i in range(n):
    num = nums[i]
    if num-1==smallest:
        count +=1
        smallest = num
    elif num-1!=smallest:
        count = 1
        smallest = num
    largest = max(largest,count)
print(largest)'''

# the below one is optimal solution
nums = [1,99,101,98,2,5,3,100,1,1]
my_set = set()
for i in range(n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    if num-1 not in my_set:
        st = num
        count = 1
        while st+1 in my_set:
            count += 1
            st +=1
        longest = max(longest,count)
print(longest)