s1 = 'abcd'
s2 = 'mnop'
s3 = '1234'
print(tuple(map(lambda a,b: a + b, s1,s2)))

print(tuple(map(lambda a,b,c: a+ b + c, s1,s2,s3)))

n = 7
print('\n'.join(list(map(lambda a:'* ' * a, range(1,n+1)))))

print('\n'.join(list(map(lambda a: '* ' * a, range(n,0,-1)))))