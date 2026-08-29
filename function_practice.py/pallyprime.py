def prime(num:int)->bool:
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False

def pallindrome(num:int)->bool:
    res = 0
    dup = num
    while num>0:
        rem = num%10
        res = res*10 + rem
        num//=10
    if dup==res:
        return True
    return False

def pallyprime(num:int)->str:
    if prime(num) and pallindrome(num):
        return 'pallyprime Number'
    return 'Not Pallyprime Number'

num = 2
print(pallyprime(num))
