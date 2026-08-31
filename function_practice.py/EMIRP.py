def prime(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False

def pallindrome(num):
    res = 0
    dup = num
    while num>0:
        rem = num%10
        res = res*10 + rem
        num//=10
    if dup!=res:
        return prime(res)
    return False

def EMIRP(num):
    if prime(num) and pallindrome(num):
        return 'EMIRP Number'
    return 'Not EMIRP Number'

num = 1
print(EMIRP(num))


print('\nMetho 2\n')

def Prime(num):
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False

def Pallindrome(num):
    res = 0
    dup = num
    while num>0:
        rem = num%10
        res = res*10 + rem
        num//=10
    if dup!=res and Prime(res):
        return True
    return False

def EMIRP_num(num):
    if Prime(num) and Pallindrome(num):
        return 'EMIRP Number'
    return 'Not EMIRP Number'

num = 1
print(EMIRP_num(num))




