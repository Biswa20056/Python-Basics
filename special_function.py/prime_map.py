def prime(val):
    if val<2:
        return 'Not Prime'
    for i in range(2,int(val**0.5)+1):
        if val%i==0:
            return f'{val} is Not Prime'
    return f'{val} is Prime'
    


print(tuple(map(prime,range(1,101))))


def Prime(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return f'{num} is not prime'
        return f'{num} is Prime'
    return f'{num} is not Prime'

print(tuple(map(Prime, range(1,101))))