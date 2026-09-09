num = 4
l = list(map(lambda sp,st:'  '* sp + st * '* ', range(num-1,-1,-1), range(1,num*2,2)))
print('\n'.join(l))

print()

l1 = list(map(lambda sp,st : '  '*sp + st * '* ', range(0,num), range((num*2)-1,0,-2)))
print('\n'.join(l1))