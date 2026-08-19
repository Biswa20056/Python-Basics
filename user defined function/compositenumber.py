def composite():
    if n>1:
        for val in range(2,int(n**0.5)+1):
            if n%val==0:
                return "Composite Number"
        return "Not Composite Number"
    return "Not Composite Number"
            
n = int(input("Enter the number : "))
print(composite())

