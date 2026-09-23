'''n = 10
factors = []
dup = n
for val in range(1,n+1):
    if n%val==0:
        factors.append(val)
print(factors)'''

n = 20
dup = n
res = []
for val in range(1,int(n**0.5)+1):
    if n%val==0:
        res.append(val)
        if n//val != val:
            res.append(n//val)
res.sort()
print(res)

'''n = 10
dup = n
res = []
for val in range(1,n//2+1):
    if n%val==0:
        res.append(val)
res.append(n)
print(res)'''

# the middle one is the optimal solution
