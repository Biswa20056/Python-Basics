var = lambda a : a*a
print(var(5))

print((lambda a:a*a)(2))

print((lambda a,b:a*b)(2,3))

print((lambda a,b=4:a*b)(4))

print((lambda a,b=5:a*b)(6,5))

# as much number of argument we will give that many values will be passed

print((lambda *args:args)(10,20,30))


print((lambda **kwargs: kwargs)(a=2,b=4))


## difference between user-defined and lambda
## we can give return keyword in user-defined function but we should not give in lambda function
## we can give multiple logic but in lambda function we can give only one logic
## to create user defined function def keyword is used but in lambda function we should not use def keyword


c = 10
print((lambda a,m:a*m)(2,c))