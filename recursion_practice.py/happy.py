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
    

print('\nmethod2\n')

def Square(num,res=0):
    if num==0:
        return res
    res = res + (num%10)**2
    return Square(num//10,res)

def is_happy(num):
    if num<10:
        return num==1 or num==7
    return is_happy(Square(num))

num = 13
if is_happy(num):
    print('Happy Number')
else:
    print('Not happy number')


print('---------------')
def sq(num):
    if num==0:
        return 0
    return (num%10)**2 + sq(num//10)

def Happy(num):
    if num<10:
        if num==1 or num==7:
            return 'happy Number'
        return 'Not Happy Number'
    return Happy(sq(num))


num = 13
print(Happy(num))
