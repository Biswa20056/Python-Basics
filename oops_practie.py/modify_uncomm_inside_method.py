class Sample:
    a = 5
    b = 10
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2
    def M1(self):
        self.val1 = 500

obj1 = Sample(200,400)
obj2 = Sample(600,800)
print(obj1.val1)
print(obj1.M1())
print(obj1.val1)
Sample.M1(obj2)
print(obj2.val1)