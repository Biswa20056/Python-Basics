def prime(num)->bool:
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False

def pallindrome(num)->int:
    dup = num
    rev = 0
    while num>0:
        rev = rev*10 + (num%10)
        num//=10
    if dup!=rev and prime(rev):
       return True
    return False    

def EMRIP(num)->str:
    if prime(num) and pallindrome(num):
        return "EMRIP Number"
    return 'Not EMRIP Number'
num = 19
print(EMRIP(num))

print('----------------------------------------')

def prime(num)->bool:
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False

def pallindrome(num)->int:
    dup = num
    rev = 0
    while num>0:
        rev = rev*10 + (num%10)
        num//=10
    return rev  

def EMRIP(num)->str:
    if prime(num) and pallindrome(num) and prime(pallindrome(num)):
        return "EMRIP Number"
    return 'Not EMRIP Number'
num = 19
print(EMRIP(num))


print('-------------------------------------------')


def prime(num)->bool:
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False

def pallindrome(num)->int:
    dup = num
    rev = 0
    while num>0:
        rev = rev*10 + (num%10)
        num//=10
    if dup!=rev and prime(rev):
       return True
    return False    

def EMRIP(num)->str:
    res = pallindrome(num)
    if prime(num) and res!= num and prime(res):
        return "EMRIP Number"
    return 'Not EMRIP Number'
num = 17
print(EMRIP(num))