nums = [[5,10,8],[7,6,3],[2,1,9]]
row = len(nums)
cols = len(nums[0])
for i in range(row):
    for j in range(cols):
        print(nums[i][j],end=' ')
    print()