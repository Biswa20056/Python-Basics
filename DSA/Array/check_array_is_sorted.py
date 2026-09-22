a = [1,2,4,7,7,5]
n = len(a)
for idx in range(n-1):
    if a[idx]>a[idx+1]:
        print('False')
        break
else:
    print('True')