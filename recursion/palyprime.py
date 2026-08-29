def pallindrome(num):
    res = 0
    if num==0:
        return 0
    res = res*10 + (num%10)
    return pallindrome(num//10)
num = 123
print(pallindrome(num))
    


















def palyprime():
    pass