def Convert_int_to_binary(num:int)->str:
    num = abs(num)
    dup = num
    place = 1
    res = 0
    while num>0:
        rem = num%2
        res = rem*place + res
        num//=2
        place*=10
    return '0b'+str(res)

num = 7
print(Convert_int_to_binary(num))