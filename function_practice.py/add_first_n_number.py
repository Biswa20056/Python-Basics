def add(num):
    res = 0
    for val in range(1,num+1):
        res +=val
    return res

num = 10
print(add(num))

print('\nMethod 2\n')

def Add(num):
    return num*(num+1)//2
num = 10
print(Add(num))