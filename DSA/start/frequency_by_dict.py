# store frequency in dictionary
# method 1
'''num = [5,6,7,5,6,7]
freq = {}
for i in range(len(num)):
    if num[i] in freq:
        freq[num[i]]+=1

    else:
        freq[num[i]] = 1
print(freq)'''
# method 2

nums = [1,2,3,4,2,3,4]
n = len(nums)
freq = {}
for i in range(n):
    freq[nums[i]] = freq.get(nums[i],0)+1

print(freq)

