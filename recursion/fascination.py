def fascinating(num,res,val):
    if val>9:
        return True
    if str(val) not in res:
        return False
    return fascinating(num,res,val+1)
    
num = 193
res = str(num*1) + str(num*2) +str(num*3)
val = 1
print(fascinating(num,res,val))

print('-------------------------------')

def fascinating(num,res,val):
    if val>9:
        return 'Fascinating Number'
    if str(val) not in res:
        return 'Not Fascinating Number'
    return fascinating(num,res,val+1)
    
num = 192
res = str(num*1) + str(num*2) +str(num*3)
val = 1
print(fascinating(num,res,val))