class A:
    def __init__(self):
        print('Hii')
    def M1(self):
        print('Hello')
class B(A):
    def __init__(self):
        print('Bye')
        A.M1(self)
        A.__init__(self)
obj1 = B()