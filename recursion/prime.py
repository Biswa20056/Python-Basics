def Prime(num,factor):
   factors = 2
   if num==0 or num==1:
      return False
   if factor<num**0.5:
        if num%factor==0:
            factors+=1
            return False
        return factors
     
   

            
    

    

num = 21
factor = 2
print(Prime(num,factor))
