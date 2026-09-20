num1 = float(input('Enter the 1st number : '))
num2 = float(input('Enter the 2nd number : '))
num3 = float(input('Enter the 3rd number : '))
if num1==num2==num3:
    print(f'{num1} and {num2} and {num3} are same')
else:
    if num1>num2:
        if num1>num3:
            print(f'{num1} is the highest number')
        else:
            print(f'{num3} is the highest number')
    else:
        if num2>num3:
            print(f'{num2} is the highets number')
        else:
            print(f'{num3} is the highest number')

print('----------------------------By elif-----------------------------')

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x == y == z:
    print(f"{x}, {y} and {z} are same")

elif x >= y and x >= z:
    print(f"{x} is the largest number")

elif y >= x and y >= z:
    print(f"{y} is the largest number")

else:
    print(f"{z} is the largest number")