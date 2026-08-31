def is_disarum(num,length):
    if num==0:
        return 0
    return (num%10)**length + is_disarum(num//10,length-1)

num = 0
length = len(str(num))
if is_disarum(num,length)==num:
    print('Disarum Number')
else:
    print('Not Disarum Number')
