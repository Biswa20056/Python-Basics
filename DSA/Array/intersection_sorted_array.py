'''a = [1,2,2,3,3,4,5,6]
b = [2,3,3,5,6,6,7]
n1 = len(a)
n2 = len(b)
visited = [0]*n2
ans = []
for i in range(n1):
    for j in range(n2):
        if a[i]==b[j] and visited[j]==0:
            ans.append(a[i])
            visited[j]=1
            break
        elif b[j]>a[i]:
            break
print(ans)'''
# the above is brute force approach
a = [1,2,2,3,3,4,5,6]
b = [2,3,3,5,6,6,7]
n1 = len(a)
n2 = len(b)
ans = []
i = 0
j = 0
while i<n1 and j<n2:
    if a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
    else:
        ans.append(a[i])
        i+=1
        j+=1
print(ans)