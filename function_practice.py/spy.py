
def digit(num):
    total = 0
    product = 1
    while num>0:
        rem = num%10
        total = total + rem
        product = product * rem
        num//=10
    if total==product:
        return True
    return False

def spy(num):
    if digit(num):
        return 'Spy Number'
    return 'Not spy Number'

num = 123
print(spy(num))
