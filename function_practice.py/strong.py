def factorial(num):
    if num>0:
        fact = 1
        for val in range(1,num+1):
            fact*=val
        return fact
    

def sum_factorial(num):
    res = 0
    while num>0:
        rem = num%10
        res = res + factorial(rem)
        num//=10
    return res

def strong(num):
    if sum_factorial(num)==num:
        return 'Strong Number'
    return 'Not Strong Number'

num = 1
print(strong(num))
