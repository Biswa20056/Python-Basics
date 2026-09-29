nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 12
def lower(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    lower_bound = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lower_bound = mid
            high = mid-1
        else:
            low = mid+1
    return lower_bound
def upper(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    upper_bound = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            upper_bound = mid
            high = mid-1
        else:
            low = mid+1
    return upper_bound

def final(nums,target):
    lb = lower(nums,target)
    if lb==-1:
        return [-1,-1]
    ub = upper(nums,target)
    return [lb,ub-1]
print(final(nums,target))
