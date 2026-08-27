<<<<<<< HEAD
def Factorial(num):
    if num<0:
        return 'Not Possible'
    elif num==0:
        return 1
    return num * Factorial(num-1)

num = 8
print(Factorial(num))
=======
def factorial(num):
    if num<0:
        return 'Not Possible'
    elif num ==0:
        return 1
    return num * factorial(num-1)
num = -1
print(factorial(num))
>>>>>>> cf920c9 (Added problems in recursion)
