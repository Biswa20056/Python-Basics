def prime(val):
    if val<2:
        return 'Not Prime'
    for i in range(2,int(val**0.5)+1):
        if val%i==0:
            return f'{val} is Not Prime'
    return f'{val} is Prime'
    


print(tuple(map(prime,range(1,101))))


def Prime(num,i):
    if i>num//2:
        return f'{num} is prime'
    if num%i==0:
        return f'{num} is not prime'
    return Prime(num,i+1)

print(tuple(map(Prime, range(1,101))))