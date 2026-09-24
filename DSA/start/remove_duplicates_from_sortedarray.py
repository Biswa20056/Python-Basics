n = [1,1,1,2,3,4,4,7,9,9,9,10]
n1 = len(n)
i = 0
j = i+1
if n1==1:
    print(n)
else:
    for idx in range(n1-1):
        if n[i]!=n[j]:
            n[i+1],n[j] = n[j],n[i+1]
            i+=1
            j+=1
        else:
            if n[i]==n[j]:
                j+=1
print(n)
print(i+1)

# by direct set 
print(set([1,1,1,2,3,4,4,7,9,9,9,10]))
print(len(set([1,1,1,2,3,4,4,7,9,9,9,10])))

# by dictionary
freq = {}
for val in n:
    if val not in freq:
        freq[val] = 1
print(list(freq.keys()))
print(len(list(freq.keys())))