def sample(num):
    if num==5:
        return
    print(num)
    num = num+1
    sample(num)
    
num = 1
sample(num)


print('------------------')



def sample1(num):
    if num==0:
        return 
    print(num)
    num = num-1
    sample1(num)

num = 10
sample1(num)



def sample1(num):
    if num==0:
        return 
    print(num)
    num = num-1
    print(sample(num))

num = 10
sample1(num)