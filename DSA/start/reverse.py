n = 1234
dup = n
rev = 0
while n>0:
    rem = n%10
    rev = rev*10+rem
    n//=10
if dup==rev:
    print('pallindrome')
else:
    print('Not pallindrome')