num = 5
l = list(map(lambda a,b:'  '* a + b * '* ' ,range(num-1,-1,-1), range(1,num+1) ))
print('\n'.join(l))