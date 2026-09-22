a = [1,2,4,7,7,5]
n = len(a)
smallest = a[0]
for idx in range(1,n):
    if a[idx]<smallest:
        smallest = a[idx]
print(smallest)
