nums = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
row = len(nums)
col = len(nums[0])
row_track = [0]*row
col_track = [0]*col
for i in range(row):
    for j in range(col):
        if nums[i][j]==0:
            row_track[i]=-1
            col_track[j]=-1
for i in range(len(row_track)):
    for j in range(len(col_track)):
        if row_track[i]==-1 or col_track[j]==-1:
            nums[i][j]=0
print(nums)