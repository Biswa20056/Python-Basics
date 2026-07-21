num = int(input("Enter the number:"))
length = len(str(num))
temp = num
res = 0
while temp>0:
    rem = temp%10
    res = res + rem**length
    temp//=10
    length-=1
if (num==res):
    print("Disroum number")
else:
    print("Not disraum number")