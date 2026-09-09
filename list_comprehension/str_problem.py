s = 'abcd'
l = []
for ind1 in range(len(s)):
    for ind2 in range(ind1+1,len(s)+1):
        k = s[ind1:ind2]
        l.append(k)
print(l)



S = 'abcd'
st = 0
end = len(s)+1
l = []
while st<end:
    for idx in range(st+1,end):
        l.append(s[st:idx])
    st+=1
print(l)
