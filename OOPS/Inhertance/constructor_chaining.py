class A():  #Parent
    def __init__(self):
        print('Hii')
        #   C.__init__(self) - Infinity loop/__init__() call.
class B(A): #Child-Parent
    def __init__(self):
        print('Hello')
        super().__init__()
class C(B): #Child
    def __init__(self):
        print('Bye')
        # by using class reference
        A.__init__(self)
        B.__init__(self)
        # by using super class
        super().__init__()
        # here in super it will call the next matching method not all the parent class 
obj1 = C()
# while using super class we should not give self keyword
