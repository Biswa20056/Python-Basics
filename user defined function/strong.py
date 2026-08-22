def sum_of_factors_of_digit(num):
    res = 0
    while num>0:
        rem = num%10
        fact = 1
        for val in range(1,rem+1):
            fact*=val
        res += fact
        num//=10
    return res

def strong(num):
    if sum_of_factors_of_digit(num) == num:
        return 'Strong Number'
    return 'Not Strong Number'

num = 145
print(strong(num))

print('--------------------------------------------')



def digits(num):
    rem = 0
    while num>0:
        rem = num%10
    return factorial(rem)
num = 123
print(digits(num))



def factorial(num):
    if num>1:
        fact = 1
        for val in range(1,num+1):
            fact *= val
        return fact
    
def Strong(num):
    sum = digits(num)
    if num==sum:
        return 'Strong Number'
    return 'Not Strong Number'

num = 123
print(Strong(num))