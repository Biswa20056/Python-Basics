nums = [5,9,1,2,4,15,6,3]
n = len(nums)
target = 130
'''def two_sum(nums,target,n):
           for i in range(n-1):
                   for j in range(i+1,n):
                           if nums[i]+nums[j]==target:
                                   return [i,j]
print(two_sum(nums,target,n))
'''

dict = {}
def find(nums,n,target):
    for i in range(n):
        remaning = target - nums[i]
        if remaning in dict:
            return [dict[remaning],i]
        dict[nums[i]] = i
    return -1

print(find(nums,n,target))
