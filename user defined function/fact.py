def factorial():
    if n>=0:
        fact = 1
        for val in range(1,n+1):
            fact*=val
        return fact
        
    else:
        return 'Factorial not possible for negativ value'
        
        
n = 4
print(factorial())