def square(num):
    if num==0:
        return 0
    return num**2
def happy(num):
    if num==1 or num==7:
        return num
    return square(num%10) + happy(num//10)

num = 13
print(happy(num))
