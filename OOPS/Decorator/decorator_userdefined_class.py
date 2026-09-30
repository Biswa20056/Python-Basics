def Outer(arg):
    print(f'arg = {arg}')
    def Inner():
        obj = arg()
    return Inner
@Outer
class Sample():
    def __init__(self):
        print('hello')
    def M1(self):
        print('M1 of sample class')
obj1 = Sample()
print(obj1.M1())