a = [10,10,10,9,8]
n = len(a)
largest = a[0]
slargest = -1
for idx in range(1,n):
    if a[idx]>largest and slargest != largest:
        slargest = largest
        largest = a[idx]
    else:
        if a[idx]<largest and a[idx]>slargest:
            slargest = a[idx]
print(slargest)