def Convert_bin_to_int(num:int)->int:
    dup = num
    power = 0
    res = 0
    while num>0:
        rem = num%10
        res = res + rem*(2**power)
        power +=1
        num//=10
    return res

num = 1000
print(Convert_bin_to_int(num))

print('-----------------------------------')
def convert2(num:str)->int:
    num = int(num[2:])
    dup = num
    power = 0
    res = 0
    while num>0:
        rem = num%10
        res = res + rem*(2**power)
        power +=1
        num//=10
    return res

num = '0b1001'
print(convert2(num))