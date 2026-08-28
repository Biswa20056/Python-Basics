def reverse(num,place):
    if num==0:
        return 0
    return (num%10)*place + reverse(num//10,place//10)


num = 345
length = len(str(num))
place = 10**(length-1)
print(reverse(num,place))