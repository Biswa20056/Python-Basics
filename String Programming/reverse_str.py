print('by negative index')
s = 'hello'
reverse = ''
st = -1
while st!=-len(s)-1:
    reverse += s[st]
    st-=1
print(reverse)

print('By positive index')

s = 'hello'
st = len(s)-1
res = ''
while st!=-1:
    res += s[st]
    st-=1
print(res)
