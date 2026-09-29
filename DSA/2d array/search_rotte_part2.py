nums = [10,11,11,12,12,12,13,13,1,2,3,7]
target = 110
def search_rotate(nums,target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[mid]<=nums[high]:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
    return False
print(search_rotate(nums,target))