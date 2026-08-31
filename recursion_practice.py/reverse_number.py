def reverse(num,place):
    if num==0:
        return 0
    return (num%10)*place + reverse(num//10,place//10)

num = 345
length = len(str(num))-1
place = 10**length
print(reverse(num,place))

print('\nMethod2\n')


def Reverse(num):
    rev = 0
    while num>0:
        rem = num%10
        rev = rev*10 + rem
        num//=10
    return rev

num = 345
print(Reverse(num))