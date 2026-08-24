def multiplication(num:int)->int:
    num = abs(num)
    return str(num*1) + str(num*2) + str(num*3)

def checking(num:int)->bool:
    res = multiplication(num)
    for val in range(1,10):
        if str(val) not in str(res):
            return False
    return True


def is_Fascination(num:int)->str:
    if checking(num):
        return 'Fascinating Number'
    return 'Not Fascinating Number'

num = 219
print(is_Fascination(num))
