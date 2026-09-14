num = 1634
dup = num
res = 0
length = len(str(num))
while num>0:
    rem = num%10
    res = res + rem**length
    num//=10
if dup==res:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')