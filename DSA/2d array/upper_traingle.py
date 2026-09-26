print('---UPPER TRIANGLE----')
nums = [[5,10,8],[7,6,3],[2,1,9]]
row = len(nums)
cols = len(nums[0])
for i in range(row):
    for j in range(cols):
        if j>=i:
            print(nums[i][j], end=' ')
    print()

print('---LOWER TRIANGLE----')
  
for i in range(row):
    for j in range(cols):
        if i>=j:
            print(nums[i][j], end=' ')
    print()

print('---DIAGONAL----')

for i in range(row):
    for j in range(cols):
        if i==j:
            print(nums[i][j], end=' ')
    print()


print('--------DIAGONAL----------')

for i in range(row):
    for j in range(cols):
        if i+j == row-1:
            print(nums[i][j], end= ' ')
    print()