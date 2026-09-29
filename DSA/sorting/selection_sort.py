nums = [5,7,3,4,1,8,9,2]
def selection(nums):
    if len(nums)<=1:
        return nums
    n = len(nums)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return nums
print(selection(nums))

# descending order

def selection_sort(nums):
    if len(nums)<=1:
        return nums
    n = len(nums)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1,n):
            if nums[j]>nums[max_idx]:
                max_idx = j
        nums[i],nums[max_idx] = nums[max_idx],nums[i]
    return nums
       
print(selection_sort(nums))