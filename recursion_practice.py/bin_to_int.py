def bin_to_int(num,power):
    if num==0:
        return 0
    return (num%10)*2**power + bin_to_int(num//10,power+1)

num = 1001
power = 0
print(bin_to_int(num,power))