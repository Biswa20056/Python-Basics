'''def Outer(arg):
    def Inner(v1,v2):
        if v1<0:
            v1 = v1*(-1)
        if v2<0:
            v2 = v2*(-1)
        return arg(v1,v2)
    return Inner
@Outer
def Func1(num1,num2):
    return num1+num2
print(Func1(5,6))
print(Func1(-3,6))
print(Func1(4,-6))
print(Func1(-1,-100))'''


def Outer(arg):
    def Inner(v1,v2):
        if v2==0:
             v2,v1 = v1,v2
        if v1==0 and v2==0:
            return 'Not Possible'
        return arg(v1,v2)
    return Inner

@Outer
def div(num1,num2):
    return num1/num2
print(div(5,10))
print(div(0,0))
print(div(0,2))
print(div(3,0))


