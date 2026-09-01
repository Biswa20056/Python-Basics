def prime(num,val=2):
    if num<2:
        return 'Not prime Number'
    if val>num**0.5:
        return 'Prime Number'
    if num%val==0:
        return 'Not Prime Number'
    return prime(num,val+1)


def pallindrome(num,power):
    if num==0:
        return 0
    return (num%10)*power + pallindrome(num//10,power//10)
  

def pallyprime(num,power):
    if prime(num)=='Prime Number' and pallindrome(num,power)==num:
        return'pallyprime Number'
    return 'Not Pallyprime Number'

num = 11
length = len(str(num))-1
power = 10**length

print(pallyprime(num,power))