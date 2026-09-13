print('Approach 2')

s = 'malayalam'
print(len(s))
for i in range(len(s)//2):
    if s[i]!=s[-i-1]:
        print(f'{s} is not pallindrome string')

        break
else:print(f'{s} is pallindrome string')