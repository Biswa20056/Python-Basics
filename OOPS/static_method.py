class Sample:
    a = 60
    b = 80
    @staticmethod
    def M1():
        print('Hello')
obj1 = Sample()
obj2 = Sample()

obj1.M1()
Sample.M1()