def prime():
    if n>1:
        for val in range(2,int(n**0.5)+1):
            if n%val==0:
                return 'Not prime'
        return 'prime number'
    return 'Not prime'

n = 6
print(prime())