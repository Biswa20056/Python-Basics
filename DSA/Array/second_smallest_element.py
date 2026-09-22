a = [1,2,4,7,7,5]
n = len(a)
smallest = a[0]
Ssmallest = float('inf')
for idx in range(1,n):
    if a[idx]<smallest:
        Ssmallest = smallest
        smallest = a[idx]
    else:
        if a[idx]!=smallest and a[idx]<Ssmallest:
            Ssmallest = a[idx]
print(Ssmallest)