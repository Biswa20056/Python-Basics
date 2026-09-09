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
