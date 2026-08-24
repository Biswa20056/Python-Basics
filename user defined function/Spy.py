def sum(num:int)->int:
    return num

def multi(num:int)->int:
    return num

def digits(num:int):
    num = abs(num)
    total = 0
    product = 1
    while num>0:
        total = total + sum(num%10)
        product = product * multi(num%10)
        num //= 10
    return total==product

def spy(num:int)->str:
    if digits(num):
        return 'Spy number'
    return 'Not spy number'

num = -1124
print(spy(num))
