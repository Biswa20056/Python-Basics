def sample():
    global num
    num = 20
    print(f'The local value : {num}')
    print(f'The memory of local value: {id(num)}')

num = 20
print(f'The global value : {num}')
print(f'The memory of global : {id(num)}')
sample()