def sample():
    global num
    num = 20
    
    print(f'The local space value:{num}')
    print(f'The memory location inside local:{id(num)}')

print(f'The global space value :{num}')
print(f'The memory location inside global:{id(num)}')
sample()