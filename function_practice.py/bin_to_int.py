def bin_to_int(num):
    res = 0
    power = 0
    dup = num
    num = abs(num)
    while num>0:
        rem = num%10
        if rem>1:
            return 'Invalid Binary Number'
        res = res + rem*(2**power)
        num//=10
        power +=1
    if dup<0:
        return res*(-1)
    return res

num = 1101
print(bin_to_int(num))

print('\nMethod 2\n')


def bin_to_int_convert(num):
    power = 0
    res = 0
    num = int(str(num[2:]))
    while num>0:
        rem = num%10
        if rem>1:
            return 'invalid Binary Number'
        res = res + rem*(2**power)
        num//=10
        power +=1
    return res

num = '0b10001'
print(bin_to_int_convert(num))