def sample():
    num = 30
    print(f'Local : {num}')
    print(f'The memory location of Local space :{id(num)}')
num = 20
print(f'Global : {num}')
print(f'The Memory location of Global Space :{id(num)}')
sample()
