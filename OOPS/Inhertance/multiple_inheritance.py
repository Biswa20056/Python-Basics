'''class A:
    pass
class B:
    pass
class C(A,B):# multiple inheritance here class c is taking proerties from both class A and class B
    pass'''

class Father:
    def func(self):
        print('More-money')
        print('Hard-Worker')
        print('Beating')
class Mother:
    def func(self):
        print('Cooking')
        print('Caring and pocket-money')
        
class Child(Father,Mother):
    def func(self):
        super().func()
        # super().func() if we wil give this then this will not execute so we will not use siper class in multiple inheritance
        Mother.func(self)
        print('Lazy')
        print('No-Money')
        print('Girlfriend')
obj1 = Child()
obj1.func()
