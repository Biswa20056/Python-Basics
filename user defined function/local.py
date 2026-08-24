def sample():
    global num
    num = 30
    print(f'local : {num}')
sample()
print(f'Global : {num}')

# global can be used for converting local variables into global

