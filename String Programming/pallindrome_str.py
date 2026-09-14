s = 'malayalam'
res = ''
st = len(s)-1
while st!=-1:
    res += s[st]
    st-=1
if res == s:
    print(f'{s} is panndrome string')
else:
    print(f'{s} is not pallindrome string')

