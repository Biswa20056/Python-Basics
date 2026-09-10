def Maximum(nums:list[int]) -> int:
    maximum = nums[0]
    for idx in range(1,len(nums)):
        if nums[idx]>maximum:
            maximum = nums[idx]
    return maximum

nums = [-1,-3,-90,-34,-100]
print(Maximum(nums))
