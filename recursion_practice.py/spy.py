def Sum(num):
    if num==0:
        return 0
    return (num%10) + Sum(num//10)

def product(num):
    if num==0:
        return 1
    return (num%10) * product(num//10)

def spy(num):
    if num==0:
        return 'Not Spy Number'
    return Sum(num)==product(num)


num = 123
print(spy(num))


print('\nMethod2\n')



def Spy(num,Total,Product):
    if num==0:
        return Total==Product
    return Spy(num//10, Total+(num%10), Product*(num%10))

num = 123
Total = 0
Product = 1
print(Spy(num,Total,Product))