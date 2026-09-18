class Sample:
    def __init__(self):
        self._a = 30
    def M1(self):
        print(self._a)
obj1 = Sample()
obj1.M1()
print(obj1._a)# the protected access can be accessible in the same package