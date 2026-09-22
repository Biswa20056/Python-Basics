arr = [3,2,1,5,2]
n = len(arr)
largest = arr[0]
for idx in range(1,n):
    if arr[idx]>largest:
        largest = arr[idx]
print(largest)
    