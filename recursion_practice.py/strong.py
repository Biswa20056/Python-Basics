def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)

def Strong(num):
    if num==0:
        return 0
    return factorial(num%10) + Strong(num//10)

num = 145
if Strong(num)==num:
    print('Strong Number')
else:
    print('Not Strong Number')