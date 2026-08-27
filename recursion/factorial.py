def Factorial(num):
    if num==0:
        return 1
    return num * Factorial(num-1)
num = 5
print(Factorial(num))

print('----------------------------')

def Factorial1(num):
    if num<0:
        return 'Not Possible'
    if num==0:
        return 1
    return num * Factorial1(num-1)

num = -1
print(Factorial1(num))