def Prime(num,factor):
  if num<2:
    return False
  if factor>num**0.5:
    return True
  if num%factor==0:
    return False
  return Prime(num,factor+1)
   
num = 12
factor = 2
print(Prime(num,factor))


print('-------------------------------')

def prime(num,factor=2):
  if num<2:
    return False
  if factor>num**0.5:
    return True
  if num%factor==0:
    return False
  return prime(num,factor+1)
   
num = 12
print(prime(num))


print('\method3\n')


print('\nmethod2\n')

def is_Prime(num,val):
    if val>num:
        return False
    if num%val==0:
        return 1 + is_Prime(num,val+1)
    return is_Prime(num,val+1)


num = 5
val = 1
if is_Prime(num,val)==2:
    print('Prime Number')
else:
    print('Not Prime Number')