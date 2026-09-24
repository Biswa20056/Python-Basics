nums = [55,32,-93,90,12,100]
n = len(nums)
largest = nums[0]
for i in range(n):
    if nums[i]>largest:
        largest = nums[i]
print(largest)

print('second method')

nums = [55,32,-93,90,12,100]
n = len(nums)
largest = nums[0]
for i in range(n):
    largest = max(largest,nums[i])
print(largest)

print(' Third method')

nums = [55,32,-93,90,12,100]
n = len(nums)
largest = float('-inf')
for i in range(n):
    largest = max(largest,nums[i])
print(largest)


print('Question for second largest')

print('Method 1')
 
nums = [55,32,-93,90,12,100]
n = len(nums)
largest = nums[0]
second_largest = float('-inf')
for i in range(n):
    if nums[i]>largest :
        second_largest = largest
        largest = nums[i]
    else:
        if nums[i]< largest and nums[i]>second_largest:
            second_largest=nums[i]
print(second_largest)

print('Method 2')

nums = [55,32,-93,90,12,100]
n = len(nums)
largest = float('-inf')
second_largest = float('-inf')
for i in range(n):
    largest = max(largest,nums[i])
for i in range(n):
    if nums[i]>second_largest and nums[i]!=largest:
        second_largest = nums[i]
print(second_largest)

print('check array is sorted or not')

nums = [5,8,9,11,12]
n = len(nums)
for i in range(n-1):
    if nums[i]>nums[i+1]:
        print('False')
        break
else:
    print('True')