def digits(num):
    if num==0:
        return 0
    rem = num%10
    num = num//10
    return rem + digits(num)
    

num = 345
print(digits(num))
