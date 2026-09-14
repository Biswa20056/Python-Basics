num = 36
l = []
for val in range(1,num+1):
    if num%val==0:
        l.append(val)
print(l)

print('optimiuze approach')

l1 = []
for val1 in range(1,int(num**0.5)+1):
    if num%val1==0:
        l1.append(val1)
        if (num//val1)!=val1:
            l1.append(num//val1)
print(sorted(l1))
