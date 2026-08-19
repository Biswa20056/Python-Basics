def sample():
    global num
    num = 30
    num = num+5
    print(f'The local space value: {num}')
    print(f'The local space value memory location: {id(num)}')
    
num = 20
print(f'The Gloabl space value1 : {num}')

sample()

print(f'The global space value2 : {num}')
print(f'The global space value memory location: {id(num)}')
