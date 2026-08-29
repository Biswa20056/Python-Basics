
def sum_of_one_to_three(num):
    return str(num*1)+str(num*2)+str(num*3)


def fascinating(num):
    for val in range(1,10):
        if str(val) not in sum_of_one_to_three(num):
            return 'Not fascinating number'
    return 'Fascinating Number'

num = 192
print(fascinating(num))
