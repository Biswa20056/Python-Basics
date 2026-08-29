def is_composite(num):
    factors = 0
    if num>1:
        for val in range(1,num+1):
            if num%val==0:
                factors+=1
        if factors>2:
            return 'Composite Number'
        return 'Not Composite Number'
    return 'Not Composite Number'
num = -4
print(is_composite(num))

print('\nMethdo 2\n')

def composite(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return 'Composite Number'
        return 'Not Composite Number'
    return 'Not Composite Number'
num = -4
print(composite(num))

print('\nMethod 3\n')

def Composite(num):
    if num >= 4:

        for val in range(2, int(num**0.5) + 1):
            if num % val == 0:
                return 'Composite Number'

    return 'Not Composite Number'
num = 4
print(Composite(num))