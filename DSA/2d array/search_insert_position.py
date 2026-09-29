nums = [1,3,4,5,8,9,14,15,19,20,21]
target = 3
def searchinsert(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    pos = n
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            pos = mid
            high = mid-1
        else:
            low = mid+1
    return pos
print(searchinsert(nums,target))
