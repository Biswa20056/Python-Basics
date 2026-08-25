def sample(num):
    print(num)
    num = num+1
    sample(num)

num = 1
print(sample(num))