def sample():
    global num
    num = 20
    print(f'The local space value:{num}')
    print(f'The memory location of local:{id(num)}')

num = 40
print(f'The global space value :{num}')
print(f'The memory location of global1 : {id(num)}')

sample()

print(f'Gloabl space value2 :{num}')
print(f'The memory loaction of Gloabl2: {id(num)}')