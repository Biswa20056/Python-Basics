def One_to_four(num):
    if num==5:
        return 0
    print(num)
    One_to_four(num+1)

num = 1
One_to_four(num)