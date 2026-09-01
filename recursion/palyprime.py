def reverse(num,place):
    if num==0:
        return 0
    return (num%10)*place + reverse(num//10,place//10)
    

def prime(num,val):
    if val>num:
        return 0
    if num%val==0:
        return 1 + prime(num,val+1)
    return prime(num,val+1)

num = 11
val = 1
place = 10**(len(str(num))-1)
if prime(num,val)==2 and reverse(num,place)==num:
    print('palyprime number')
else:
    print('Not palyprime number')

