def Disarum(num,length):
    length = len(str(num))
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

def Disarum(num):
    length = len(str(num))
    if length==0:
        return 0
    return (num%10)**length + Disarum(num//10)

num = 153
if Disarum(num)==num:
    print('Disarum Number')
else:
    print('Not Disarum Number')