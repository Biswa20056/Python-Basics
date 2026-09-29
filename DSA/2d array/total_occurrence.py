nums = [1,2,3,3,3,3,3,4,6,7,8,11,12,12,12]
target = 3
def lowerbound(nums,target):
    n = len(nums)
    lb = -1
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb
def upperbound(nums,target):
    n = len(nums)
    ub = n
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub
def frequency(nums,target):
    lb = lowerbound(nums,target)
    if lb==-1:
        return 0
    ub = upperbound(nums,target)
    return ub-lb

print(frequency(nums,target))