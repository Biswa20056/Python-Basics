def reverse(num):
    rev = 0
    dup = num
    num = abs(num)
    while num>0:
        rem = num%10
        rev = rev*10 + rem
        num//=10
    if dup<0:
        return rev*(-1)
    return rev

num = -123
print(reverse(num))