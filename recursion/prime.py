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