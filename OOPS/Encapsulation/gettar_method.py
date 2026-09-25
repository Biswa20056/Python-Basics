class sample:
    def __init__(self):
        self.__a = 30
    def gettar(self):
        return self.__a


obj = sample()
print(obj.gettar())
#print(obj.__a) this will raise error bcoz a is now private data
# gettar methof is used to acces the private data outside the class
