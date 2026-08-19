def reverse_number(num:int)->int:
    dup = num
    num = abs(num)
    rev = 0
    while num>0:
        rem = num%10
        rev = rev*10 + rem
        num//=10
    if dup<0:
        return rev*(-1)
    return rev

num = 123
print(reverse_number(num))