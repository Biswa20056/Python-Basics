def int_to_binary(num,place):
    if num==0:
        return 0
    return (num%2)*place + int_to_binary(num//2,place*10)

num = 12
place = 1
print(int_to_binary(num,place))

print('-----------------------------------')

def int_to_binary(num,place):
    if num==0:
        return 0
    return (num%2)*place + int_to_binary(num//2,place*10)

num = 12
intial = 10
power = 0
place = intial**power

print(int_to_binary(num,place))
