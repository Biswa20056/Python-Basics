nums = [1,2,5,3,0,-10,-100,34,67,-98]
target = 34
n = len(nums)
found = -1
for i in range(n):
    if nums[i]==target:
        found = i
print(found)

def linear(nums,target):
    for i in range(n):
        if nums[i]==target:
            return i
    return -1
print(linear(nums,target))