
def square(num)->int:
    return num**2

def digit(num)->int:
    total = 0
    while num>0:
        total += square(num%10)
        num//=10
    if total>9:
        return digit(total)
    return total

def is_happy(num:int)->str:
    if digit(num) == 1 or digit(num)==7:
        return 'Happy Number'
    return 'Not Happy Number'

num = 45
print(is_happy(num))


print('---------------------------------')

def sq(num:int)->int:
    res = 0
    while num>0:
        res += (num%10)**2
        num//=10
    return res

def is_Happy(num:int)->str:
    while num>9:
        num = sq(num)
    if num==1 or num==7:
        return 'HAppy Number'
    return 'Not Happy Number'

num = -1
print(is_happy(num))

print('----------------------------------')

def sq(num:int)->int:
    res = 0
    while num>0:
        res += (num%10)**2
        num//=10
    return res

def is_Happy(num:int)->str:
    while num>9:
        num = sq(num)
    if num in (1,7):
        return 'Happy Number'
    return 'Not Happy Number'

num = -1
print(is_happy(num))