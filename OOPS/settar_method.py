class Sample:
    def __init__(self):
        self.__a = 30
    def gettar(self):
        return self.__a
    def settar(self):
        self.__a = 100

obj = Sample()
print(obj.gettar())
print(obj.settar())
print(obj.gettar())