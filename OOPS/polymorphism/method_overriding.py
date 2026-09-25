class A:
    def M1(self):
        print('M1 of class A')
    def M2(self):
        print('M2 of class A')
class B:
    def M1(self):
        print('M1 of class B')
    def M2(self):
        print('M2 of class B')
obj = B()
obj.M1()
# chaining is opposite to method over riding
# thsi is also calles run time polymorphism
# multiple class contains sam emethod name but different functionalities then the method in the parent class is overridden by the method in the child class
