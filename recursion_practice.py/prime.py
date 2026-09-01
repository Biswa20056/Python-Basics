def prime(num,val=2):
    if num<2:
        return 'Not prime Number'
    if num%val==0:
        return 'Not prime Number'
    if val>num**0.5:
        return 'Prime Number'
    return prime(num,val+1)

num = 31
print(prime(num))   


print('\nmethod2\n')

def Prime(num,val):
    if val>num:
        return False
    if num%val==0:
        return 1 + Prime(num,val+1)
    return Prime(num,val+1)


num = 5
val = 1
if Prime(num,val)==2:
    print('Prime Number')
else:
    print('Not Prime Number')