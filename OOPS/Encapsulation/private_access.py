class Sample:
    def __init__(self):
        self.__a = 30
    def M1(self):
        print(self.__a)
        self.__M2()
    def __M2(self):
        print('Hello')
obj1 = Sample()
obj1.M1()
# print(obj1.__a) this statement will give error bcoz we can access the private access inside class only
# obj1.__M2() this is  not accessible
# the private data and private methods can be accessed inside the class only
