a = [10,20,30,40,50]
target = 90
n = len(a)
found = -1
for idx in range(n):
    if a[idx]==target:
        found = idx
        break
print(found)