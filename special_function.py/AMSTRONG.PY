def Amstrong(num):
    if num>0:
        length = len(str(num))
        res = 0
        dup = num
        while num>0:
            rem = num%10
            res = res + rem**length
            num//=10
        if dup==res:
            return f'{dup} is a Amrmstrong Number'
        return f'{dup} is not a Armstrong Number'
    return f'{dup} is not Armstrong Number'

print(list(map(Amstrong, range(1,10001))))