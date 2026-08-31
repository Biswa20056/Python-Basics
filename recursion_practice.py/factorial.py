def factorial(num):
    if num<0:
        return 'Not possible'
    if num==0:
        return 1
    return num * factorial(num-1)

num = -5
print(factorial(num))