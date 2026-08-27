def Amstrong(num):
    if num==0:
        return 0
    return (num%10) ** length + Amstrong(num//10)

num = 152
length = len(str(num))
if num == Amstrong(num):
    print ('Amstrong Number')
else:
    print('Not Amstrong Number')

print('------------------------------------------')

def Amstrong(num,length):
    if num==0:
        return 0
    return (num%10) ** length + Amstrong(num//10,length)

num = 152
length = len(str(num))
if num == Amstrong(num,length):
    print ('Amstrong Number')
else:
    print('Not Amstrong Number')

# the number of arguments are inside the function call the same number of parameters should be present in the function call also
