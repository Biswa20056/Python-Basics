def sample():
    print(f'Local:{num}')

print(f'Global:{num}')
num = 10# it wil throw error bcoz we have not declared num before declaring we are printing so name error
sample()
print(f'Global:{num}')



