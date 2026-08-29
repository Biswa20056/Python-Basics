def factorial(num):
    if num==0:
        return 1
    return num * factorial(num-1)

def strong(num):
    if num==0:
        return 0
    return factorial(num%10) + strong(num//10)


num = 146
if strong(num)==num:
    print('Strong Number')
else:
    print('Not Strong Number')