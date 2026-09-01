def square(num):
    if num==0:
        return 0
    return (num%10)**2 + square(num//10)

def happy(num):
    if num==1 or num==7:
        return True
    if num==4:
        return False
    return happy(square(num))

num = 14
if happy(num):
    print('Happy Number')
else:
    print('Not Happy Number')
    