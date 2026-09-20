w = int(input("Enter the 1st number : "))
x = int(input("Enter the 2nd number : "))
y = int(input("Enter the 3rd number : "))
z = int(input("Ente rthe 4th number : "))
if w==x==y==z:
    print('All are same')
else:
    if w>x:
        if x>y:
            if w>z:
                print(f'{w} is the largest one')
            else:
                print(f'{z} is the largest one')
        else:
            if y>z:
                print(f'{y} is the largest one')
            else:
                print(f'{z} is the largest one')
    else:
        if x>y:
            if x>z:
                print(f'{x} is the largest one')
            else:
                print(f'{z} is the largest one')
        else:
            if y>z:
                print(f'{y} is the largest one')
            else:
                print(f'{z} is the largest one')

print('---------------By elif-------------------')
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
c = int(input("Enter the 3rd number : "))
d = int(input("Enter the 4th number : "))
if a==b==c==d:
    print('All are same')
elif a>b and a>c and a>d:
    print(f'{a} is the largest one')
elif b>c and c>d:
    print(f'{b} is the largest one')
elif c>d:
    print(f'{c} is the largest one')
else:
    print(f'{d} is the largest one')