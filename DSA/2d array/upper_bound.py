nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 1
def upperbound(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    upper_bound = n
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>target:
            upper_bound = mid
            high = mid-1
        else:
            low = mid+1
    return upper_bound
print(upperbound(nums,target))
