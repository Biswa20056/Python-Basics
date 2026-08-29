def Sum(num):
    if num==0:
        return 0
    return (num%10) + Sum(num//10)
def Multi(num):
    if num==0:
        return 1
    return (num%10) * Multi(num//10)
def spy(num):
    return Sum(num)==Multi(num)

num = 122
print(spy(num))


print('---------------------------')



def Spy(num,total,multi):
    if num==0:
        if total==multi:
            return 'Spy number'
        else:
            return 'Not Spy number'
    return Spy(num//10, total+(num%10), multi*(num%10))

num = 123
total = 0
multi = 1
print(Spy(num,total,multi))