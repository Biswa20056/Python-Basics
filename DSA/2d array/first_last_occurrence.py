nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 3
def first_last(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    first = -1
    last = -1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            last = mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return last
print(first_last(nums,target))
