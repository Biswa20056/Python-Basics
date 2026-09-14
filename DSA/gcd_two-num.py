n1 = 20
n2 = 40
gcd = 1
for val in range(1,n1+1):
    if n1%val==0 and n2%val==0:
        gcd = val
print(gcd)


print('Optimized Approach')

a = 12
b = 9
for val in range(min(a,b),1,-1):
    if a%val==0 and b%val==0:
        print(val)
        break

print('Best Approach - equilidean algorithm')

x = 52
b = 10
while a>0 and b>0:
    if a>b:
        a = a%b
    else:b = b%a
if a==0:
    print(b)
else:print(a)