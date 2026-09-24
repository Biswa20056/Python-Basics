# if a python file contains more than 2 types of inheritance it is called hybrid inheritance
class A:
    def __init__(self,var1):
        self.var1=var1
    def display(self):
        print(self.var1)
class B(A):
    def __init__(self,var2):
        super().__init__(60)
        self.var2=var2
    def display(self):
        super().display()
        print(self.var2)
class C(A):
    def __init__(self,var3):
        super().__init__(50)
        self.var3=var3
    def display(self):
        super().display()
        print(self.var3)
class D(B,C):
    def __init__(self,var4):
        super().__init__(40)
        self.var4=var4
    def display(self):
        super().display()
        print(self.var4)
class E(B,C):
    def __init__(self,var5):
        super().__init__(30)
        self.var5=var5
    def display(self):
        super().display()
        print(self.var5)
class F(D,E):
    def __init__(self,var6):
        self.var6=var6
        super().__init__(20)
    def display(self):
        super().display()
        print(self.var6)

ob1=F(10)
ob1.display()
print(F.mro())