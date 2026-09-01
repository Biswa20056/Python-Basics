def sum_of_first_n_number(num):
    if num==11:
        return 0
    return num + sum_of_first_n_number(num+1)

num = 1
print(sum_of_first_n_number(num))
