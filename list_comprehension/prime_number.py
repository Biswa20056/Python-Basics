num= -2

print('Prime Number' if (len([val for val in range(1,num+1) if num%val==0]))==2 else 'Not Prime Number')

print('prime number' if num>1 and  len([val for val in range(2,int(num**0.5)+1) if num%val==0]) == 0 else 'Not Prime')