class A():
    def __init__(self):
        print('Hii')
class B(A):
    def __init__(self):
        print('Hello')
class C(B):
    def __init__(self):
        print('Bye')
        # by using class reference
        A.__init__(self)
        B.__init__(self)
        # by using super class
        super().__init__()
        # here in super it will call the next matching method not all the parent class 
obj1 = C()
