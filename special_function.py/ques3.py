n = 5
l = list(map(lambda sp,st: '  '* sp + st * '* ', range(0,n), range(n,0,-1)))
print('\n'.join(l))