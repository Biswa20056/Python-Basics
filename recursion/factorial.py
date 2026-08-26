def Factorial(num):
    if num<0:
        return 'Not Possible'
    elif num==0:
        return 1
    return num * Factorial(num-1)

num = 8
print(Factorial(num))