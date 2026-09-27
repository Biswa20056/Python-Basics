nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
row = len(nums)
col = len(nums[0])
'''res = [[0 for i in range(col)] for j in range(row)]
res_col = 0
for i in range(row-1,-1,-1):
    for j in range(col):
        res[j][res_col] = nums[i][j]
    res_col+=1
print(res)
'''
# optimal in place solution

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
row = len(nums)
col = len(nums[0])
for i in range(row-1):
    for j in range(i+1,col):
        nums[i][j],nums[j][i] = nums[j][i],nums[i][j]
for i in range(row):
    nums[i].reverse()
print(nums)