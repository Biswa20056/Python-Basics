def int_to_bin(num,place):
    if num==0:
        return 0
    return (num%2)*place + int_to_bin(num//2,place*10)

num = 9
val = 10
power = 0
place = val**power
print(int_to_bin(num,place))