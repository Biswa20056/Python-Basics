def Outer(arg):
    def Inner(v1,v2):
        if v1<0:
            v1 = v1*(-1)
        if v2<0:
            v2 = v2*(-1)
        return arg(v1,v2)
    return Inner
@Outer
def func1(num1,num2):
    return num1+num2

print(func1(4,6))
print(func1(2,-1))
print(func1(-2,-4))