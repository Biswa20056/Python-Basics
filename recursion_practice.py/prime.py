def prime(num,val=2):
    if num<2:
        return 'Not prime Number'
    if val>num**0.5:
        return 'Prime Number'
    if num%val==0:
        return 'Not prime Number'
    return prime(num,val+1)

num = 31
print(prime(num))   