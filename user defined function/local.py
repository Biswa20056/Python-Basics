def sample():
    global num
    num = 30
    print(f'local : {num}')
sample()
print(f'Global : {num}')
