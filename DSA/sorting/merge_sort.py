def Merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left_side = nums[:mid]
    right_side = nums[mid:len(nums)]
    left = Merge_sort(left_side)
    right = Merge_sort(right_side)
    return merge_array(left,right)

def merge_array(left,right):
    res = []
    m = len(left)
    n = len(right)
    i = 0
    j = 0
    while i < m and j < n:
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    if i<m:
        while i<m:
            res.append(left[i])
            i+=1
    if j<n:
        while j<n:
            res.append(right[j])
            j+=1
    return res

nums = [3,1,2,4,1,5,2,6,4]
print(Merge_sort(nums))