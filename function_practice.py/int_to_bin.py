def Convert_int_to_bin(num):
    res = 0
    place = 1
    while num>0:
        rem = num%2
        res = res + rem*place
        place *= 10
        num//=2
    return res

num = 13
print(Convert_int_to_bin(num))


print('\nMethod 2\n')


def convert(num):
    num = abs(num)
    dup = num
    place = 1
    res = 0
    while num>0:
        rem = num%2
        res = res = rem*place
        num//=2
        place *= 10
    return '0b' + str(res)
num = 8
print(convert(num))

print('\nMethod 3\n')

def convert_int(num):
    res = ''
    while num>0:
        rem = str(num%2)
        res = str(res) + rem
        num//=2
    return '0b' + res

num = 8
print(convert_int(num))
