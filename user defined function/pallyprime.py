def prime(num)->bool:
    if num>1:
        for val in range(2,int(num**0.5)+1):
            if num%val==0:
                return False
        return True
    return False
def pallindrome(num)->int:
    rev = 0
    while num>0:
        rev = rev*10 + (num%10)
        num//=10
    return rev

def pallyprime(num)->str:
    if prime(num) and (pallindrome(num)==num):
        return "Pallyprime Number"
    return "Not Pallyprime Number"
num = 2
print(pallyprime(num))
