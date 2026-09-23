n = 153
dup = n
power = len(str(n))
res = 0
while n>0:
    rem = n%10
    res = res + rem**power
    n//=10
if dup==res:
    print('True')
else:
    print('False')