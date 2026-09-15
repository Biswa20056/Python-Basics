class Sample:
    x = 10
    y = 20
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    def M1(self):
        print(self.val1,self.val2)

obj1 = Sample(500,100)
obj2 = Sample(10000,20000)

print(obj1.val2)
print(obj2.val1)
obj1.M1()# accessing the method by object ref 
obj2.M1()

Sample.M1(obj1)# accessing the methods by class ref
Sample.M1(obj2)