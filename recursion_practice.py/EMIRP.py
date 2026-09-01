def prime(num,val=2):
    if num<2:
        return False
    if val>num**0.5:
        return True
    if num%val==0:
        return False
    return prime(num,val+1)

def pallindrome(num,power):
    if num==0:
        return 0
    return (num%10)*power + pallindrome(num//10,power//10)


def EMIRP(num,power):
    rev = pallindrome(num,power)
    if prime(num) and rev!=num and prime(rev):
        return 'EMIRP Number'
    return 'NOT EMIRP Number'

num = 13
length = len(str(num))-1
power = 10**length
print(EMIRP(num,power))