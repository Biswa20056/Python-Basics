def Is_Armstrong(num):
    if num>0:
        length = len(str(num))
        dup = num
        res = 0
        while num>0:
            rem = num%10
            res = res + rem**length
            num//=10
        if dup==res:
            return 'Armstrong Number'
        return 'Not Armstrong Number'
    return 'Not Possible'

num = -153
print(Is_Armstrong(num))
