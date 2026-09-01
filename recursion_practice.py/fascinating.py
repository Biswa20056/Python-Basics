def fascinating(num,ans,val=1):
    if val>9:
        return True
    if str(val) not in ans:
        return False
    return fascinating(num,ans,val+1)


num = 191
ans = str(num*1) + str(num*2) + str(num*3)
print(fascinating(num,ans))