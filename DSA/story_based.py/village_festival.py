def second_largest(nums):
    n = len(nums)
    max_element = nums[0]
    second_max = float('-inf')
    for i in range(n):
        if nums[i] > max_element and max_element != second_max:
            second_max = max_element
            max_element = nums[i]
        else:
            if nums[i] < max_element and  nums[i] > second_max :
                second_max = nums[i]
    return second_max

nums = [12,45,7,89,23,56,34]
print(second_largest(nums))
