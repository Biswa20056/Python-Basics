def binary_to_int(num,power):
    if num==0:
        return 0
    return (num%10)*(2**power) + binary_to_int(num//10,power+1)
    
num = 1100
power = 0
print(binary_to_int(num,power))