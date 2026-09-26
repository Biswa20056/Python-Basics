def setinfinite(nums,row,col):
    r = len(nums)
    c = len(nums[0])
    for i in range(r):
        if nums[i][col]!=0:
            nums[i][col]=float('inf')
    for j in range(c):
        if nums[row][j]!=0:
            nums[row][j]=float('inf')

def setzero(nums):
    row = len(nums)
    col = len(nums[0])
    for i in range(row):
        for j in range(col):
            if nums[i][j]==0:
                setinfinite(nums,i,j)

    for i in range(row):
        for j in range(col):
            if nums[i][j]==float('inf'):
                nums[i][j]=0
    return nums
    

nums = [[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
print(setzero(nums))
