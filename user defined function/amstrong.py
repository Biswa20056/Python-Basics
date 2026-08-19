def Check_Amstrong(num:int)->str:
     #  The part inside parenthesis is called as function annotations(num:int)-> 
    if num>0:
        digits = len(str(num))
        dup = num
        res = 0
        while num>0:
            rem = num%10
            res = res + rem**digits
            num//=10
        if dup==res:
            return True
        return False
    return "Not an Armstrong Number"
num = 198
print(Check_Amstrong(num))