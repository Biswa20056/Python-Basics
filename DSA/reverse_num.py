n = 9877
dup = abs(n)
rev = 0
while dup>0:
    rem = dup%10
    rev = rev*10 + rem
    dup//=10
if n<0:
    print(rev*-1)
else:print(rev)