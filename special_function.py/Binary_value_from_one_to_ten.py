def binary_value(num):
    place = 1
    binary = 0
    dup = num
    while num>0:
        rem = num%2
        binary = binary + rem*place
        num//=2
        place*=10
    return f'The binary of {dup} is {binary}'

print(tuple(map(binary_value,range(1,11))))
