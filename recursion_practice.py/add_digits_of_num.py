def Add_digit(num):
    if num==0:
        return 0
    return (num%10) + Add_digit(num//10)

num = -134
print(Add_digit(num))