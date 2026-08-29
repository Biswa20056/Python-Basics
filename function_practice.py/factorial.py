def Factorial(num):
    fact = 1
    if num<0:
        return 'Not possible'
    if num==0 or num==1:
        return 1
    for val in range(1,num+1):
        fact *= val
    return fact

num = -1
print(Factorial(num))


print('\nMethod 2\n')


def factorial(num):
    if num>=0:
        fact = 1
        for val in range(1,num+1):
            fact *= val
        return fact
    return 'Not possible'
num = 0
print(factorial(num))