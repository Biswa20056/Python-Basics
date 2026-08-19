def add():
    return n*(n+1)//2
n = 5
print(add())

print('-----------------------')

def add1():
    res = 0
    for val in range(1,n+1):
        res+=val
    return res
n = int(input("Enter the number : "))
print(add1())

print('-------------------------')

def add2():
    res = 0
    global n
    while n>0:
        res+=n
        n-=1
    return res
n = int(input("Enter the number : "))
print(add2())