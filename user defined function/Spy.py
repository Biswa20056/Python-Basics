def sum(num:int)->int:
    total = 0
    return num + total

def multi(num:int)->int:
    product = 1
    return num*product

def digits(num:int):
    num = abs(num)
    while num>0:
        total = sum(num%10)
        product = multi(num%10)
        num //= 10
    return total==product

def spy(num:int)->str:
    if digits(num):
        return 'Spy number'
    return 'Not spy number'

num = 123
print(spy(num))
