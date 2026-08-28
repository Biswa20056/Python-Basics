def reverse(num):
    if num==0:
        return ""
    return str(num%10) + reverse(num//10)
num = 345
print(reverse(num))