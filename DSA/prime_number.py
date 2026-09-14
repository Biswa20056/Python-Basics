n = 2
factor = 0
if n>1:
    for val in range(1,int(n**0.5)+1):
        if n%val==0:
            factor+=1
            if (n//val)!=val:
                factor+=1
    if factor==2:
        print('Prime')
    else:
        print('Not Prime')
else:print('Not Prime')