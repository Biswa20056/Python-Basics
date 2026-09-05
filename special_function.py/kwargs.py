print((lambda **kwargs: kwargs)(a=2,b=4))


## difference between user-defined and lambda
## we can give return keyword in user-defined function but we should not give in lambda function
## we can give multiple logic but in lambda function we can give only one logic
## to create user defined function def keyword is used but in lambda function we should not use def keyword

def  EvenOdd(val):
    if val%2==0:
        return 'Even'
    return 'Odd'

print(list(map(EvenOdd, range(1,11))))


def  EvenOdd1(val):
    if val%2==0:
        return 'Even'

print(list(map(EvenOdd1, range(1,11))))

def  EvenOdd2(val):
    if val%2==0:
        return 'Even'
    return 'Odd'

print(str(map(EvenOdd2, range(1,11))))

def  EvenOdd3(val):
    if val%2==0:
        return f'{val} is Even'
    return f'{val} is Odd'

print(list(map(EvenOdd3, range(1,11))))