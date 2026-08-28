def Sum(num):
    if num==0:
        return 0
    return (num%10) + Sum(num//10)
def Multi(num):
    if num==0:
        return 1
    return (num%10) * Multi(num//10)
def Spy(num):
    if num==0:
        return 0
    return Sum(num)==Multi(num)

num = 122
print(Spy(num))