class Sample:
    a = 6
    b = 9
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def M1(self):
        self.v1 = 1000 # in this way we can modify the un-common property inside the object method
        # object method is the only way to modify the un-common property inside class
        print(self.v1,self.v2)# here in place of self if we will write obj1 or obj2 it will raise error

obj1 = Sample(500,600)
obj2 = Sample(700,800)

# access object method through object reference
obj1.M1()
obj2.M1()
# access object method through class reference
Sample.M1(obj1)
Sample.M1(obj2)