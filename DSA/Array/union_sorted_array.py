'''a1 = [1,1,2,3,4,5]
a2 = [2,3,4,4,5,6]
s = set()
for i in range(len(a1)):
    s.add(a1[i])
for i in range(len(a2)):
    s.add(a2[i])
print(list(s))'''
# the above solution is brute force approach
a1 = [1,1,2,3,4,5]
a2 = [2,3,4,4,5,6]
n1 = len(a1)
n2 = len(a2)
i = 0
j = 0
ans = []
while i<n1 and j<n2:
    if a1[i]<a2[j]:
        if not ans or ans[-1]!=a1[i]:
            ans.append(a1[i])
        i+=1
    elif a2[j]<a1[i]:
        if not ans or ans[-1]!=a2[j]:
            ans.append(a2[j])
        j+=1
    else:
        if not ans or ans[-1]!=a1[i]:
            ans.append(a1[i])
        i+=1
        j+=1
while i<n1:
    if not ans or ans[-1]!=a1[i]:
        ans.append(a1[i])
    i+=1

while j<n2:
    if not ans or ans[-1]!=a2[j]:
        ans.append(a2[j])
    j+=1

print(ans)
