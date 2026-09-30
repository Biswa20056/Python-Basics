nums = [1,2,3,4,5,9,6,7]
def bubble_sort(nums):
    if len(nums)<=1:
        return nums
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums   
print(bubble_sort(nums))
         