def add_square_digit(num):
    return num**2


def digit(num):
    res = 0 
    while num>0:
        rem = num%10
        res = res + add_square_digit(rem)
        num//=10
    if res>9:
        return digit(res)
    return res

def happy(num):
    if digit(num)==1 or digit(num)==7:
        return 'Happy number'
    return 'Not Happy Number'

num = 13
print(happy(num))