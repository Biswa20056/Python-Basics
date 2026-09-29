nums = [1,2,3,4,5,8,9,12,13]
'''target = 5
def binary_search(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low + high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1
print(binary_search(nums,target))'''

# recursice approach

nums = [1,2,3,4,5,8,9,12,13]
n = len(nums)
low = 0
high = n-1
target = 5
def binarysearch(nums,low,high,target):
    if low>high:
        return -1
    mid = (low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        return binarysearch(nums,low,mid-1,target)
    else:
        return binarysearch(nums,mid+1,high,target)
print(binarysearch(nums,low,high,target))