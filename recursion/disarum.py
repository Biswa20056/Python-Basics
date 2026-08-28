def Disarum(num,length):
    if length==0:
        return 0
    return (num%10)**length + Disarum(num//10,length-1)

num = 153
length = len(str(num))
if Disarum(num,length)==num:
    print('Disarum Number')
else:
    print('Not Disarum Number')

print('-------------------------------')

