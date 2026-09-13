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

print('Approach 2')

s = 'malayalam'
st = 0
end = len(s)-1
while st!=end:
    if s[st]==s[end]:
        st+=1
        end-=1
    else:
        print('{s} is not pallindrome')