class A():
    v1 = 30
    v2 = 50
    def M2(self):
        print('Hello')
class B(A):
    v3 = 100
    v1 = 10
    def M1(self):
        print('World')

obj1 = B()
obj1.M1()
obj1.M2()