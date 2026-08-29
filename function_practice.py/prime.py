def prime(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return 'Not prime Number'
        return 'Prime Number'
    return 'Not prime Number'
num = -2
print(prime(num))

print('\nMethod2\n')

def Prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return 'Not Prime Number'
        return 'Prime Number'
    return 'Not Prime Number'
num = -2
print(Prime(num))


print('\nMethod3\n')


def prime_number(num):
    factor = 0
    if num>1:
        for val in range(2,num):
            if num%val==0:
                factor+=1
        if factor>2:
            return 'Not Prime Number'
        return 'Prime Number'
    return 'Not prime Number'

num = -2
print(prime_number(num))

print('\nmethod4\n')

def prime_num(num):
    factors = 0
    if num>1:
        for val in range(1,num+1):
            if num%val==0:
                factors+=1
        if factors==2:
            return 'Prime Number'
        return 'Not Prime Number'
    return 'Not Prime Number'

num = -2
print(prime_num(num))

