nums = [[5,9,1],[2,3,7]]
row = len(nums)
col = len(nums[0])
res = [[0]*row for _ in range(col)]
for i in range(row):
    for j in range(col):
        res[j][i] = nums[i][j]
print(res)

