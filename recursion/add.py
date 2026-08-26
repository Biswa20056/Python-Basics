def add(num):
    if num==6:
        return 0
    return num + add(num+1)
    
num = 1
print(add(num))
