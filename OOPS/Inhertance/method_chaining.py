class A():
    v1 = 3
    v2 = 50
    def M1(self):
        print('M1 method of clss A')
class B(A):
    v3 = 100
    v1 = 10
    def M1(self):
        # chaing by super class
        super().M1()
        print('M1 method of class B')
        # chaing by class ref
        A.M1(self)
obj1 = B()
obj1.M1()
'''
while perrforming by class reference we do not have to give the inheritance means if we will write class B() it will not throw any error
but while dealing with super class we have to pass the inheritance 
and while delaing with the super clas we do not have to give the self for the methods
'''