def reverse(num,place):
    if num==0:
        return 0
    return (num%10)*place + reverse(num//10,place//10)

num = 345
length = len(str(num))
place = 10**(length-1)
print(reverse(num,place))

print('\nCheck Pallindrome or not\n')



def reverse(num,place):
    if num==0:
        return 0
    return (num%10)*place + reverse(num//10,place//10)

num = 121
length = len(str(num))
place = 10**(length-1)
if reverse(num,place)==num:
    print('pallindrome Number')
else:
    print('Not pallindrome Number')
    