def Is_Armstrong(num,length)->str:
    if num==0:
        return 0
    return (num%10)**length + Is_Armstrong(num//10,length)

num = 153
length=len(str(num))
if Is_Armstrong(num,length)==num:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')


print('\nMethod 2\n')


def Armstrong(num):
    if num==0:
        return 0
    return (num%10)**length + Armstrong(num//10)

num = 153
length = len(str(num))
if Armstrong(num)==num:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')

    