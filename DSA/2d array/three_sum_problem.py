arr = [-1,0,1,2,-1,-4]
'''my_set = set()
i = 0
j = i+1
k = j+1
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] == 0:
                temp = [arr[i], arr[j], arr[k]]
                temp.sort()
                my_set.add(tuple(temp))
for ans in my_set:
    print(list(ans))'''
    # the above is brute force approach

    # the below one is Better
'''arr = [-1,0,1,2,-1,-4]
n = len(arr)
res = set()
for i in range(n):
    my_set = set()
    for j in range(i+1,n):
        third = -(arr[i]+arr[j])
        if third in my_set:
            temp = [arr[i],arr[j],third]
            temp.sort()
            res.add(tuple(temp))
        my_set.add(arr[j])
for ans in res:
    print(list(ans))
'''
# the below code is optimal

arr = [-1,0,1,2,-1,-4]
n = len(arr)
ans = []
arr.sort()
for i in range(n):
    if i!=0 and arr[i]==arr[i-1]:
        continue
    j = i+1
    k = n-1
    while j<k:
        total_sum = arr[i] + arr[j] + arr[k]
        if total_sum < 0:
            j+=1
        elif total_sum > 0:
            k-=1
        else:
            temp = [arr[i], arr[j], arr[k]]
            ans.append(temp)
            j+=1
            k-=1
            while j<k and arr[j] == arr[j-1]:
                j+=1
            while j<k and arr[k] == arr[k+1]:
                k-=1
print(ans)
