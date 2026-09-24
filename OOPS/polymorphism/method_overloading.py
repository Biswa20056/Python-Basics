'''class Sample:
    def M1(self,a):
        print(a)
    def M1(self,a,b):# since the method are same this will replace the previous method
        print(a+b)
    def M1(self,a,b,c):# since the method are same this will replace the previous method , now this is the only method inside the class
        print(a+b+c)
obj1 = Sample()
obj1.M1(5,10,15)'''
# we can give different functionality by default parameter or variable length non key-word argumen

'''class Sample():
    def M1(self,a):
        print(a)
    def M1(self,a,b):
        print(a+b)
    def M1(self,a=10,b=15,c=5):
        print(a+b+c)
obj1 = Sample()
obj1.M1()
obj1.M1(5)
obj1.M1(1,2)
obj1.M1(12,23,34)'''
# obj1.M1(1,2,3,4)# this will thriw error

# method overloading by variable length non keyword argument (*args)

class Sample:
    def M1(self,a):
        print(a)
    def M1(self,a,b):
        print(a+b)
    def M1(self,*args):
        res = 0
        for val in args:
            res += val
        print(res)
obj1 = Sample()
obj1.M1(10,20,30,40,50)
