'''class A():
    v1 = 40
    v2 = 50
class B(A):
    v2 = 60
    v3 = 90
class C(B):
    v3 = 100
    v1 = 10

obj = C()
print(obj.v1)
print(obj.v3)'''
# print(obj.v5) it will raise error
# it alsways gives the latest value
'''
If there is the variable then give the value or if there is no variable and some inheritance is there then check in that class 
whether the variable is there or not
'''

class V1:
    def __init__(self,message,DP):
        self.messgae = message
        self.DP = DP
    def Display(self):
        print(self.messgae)
        print(self.DP)

# creating version 2 while the version 1 willbe there nothing will erased
class V2(V1):
    def __init__(self,message,DP,Status,AudioCall):
        super().__init__(message,DP)# her we can give class ref also 
        self.Status = Status
        self.AudioCall = AudioCall
    def Display(self):
        V1.Display(self)
        print(self.Status)
        print(self.AudioCall)

class V3(V2):
    def __init__(self,message,DP,Status,AudioCall,AI,Payments):
        #super().__init__(message,DP,Status,AudioCall) by using super class() reference
        V2.__init__(self,message,DP,Status,AudioCall)
        self.AI = AI
        self.Payments = Payments
    def Display(self):
        V1.Display(self)
        V2.Display(self)
        print(self.AI)
        print(self.Payments)

obj1 = V3('Hi','No','Good Morning','30-min','yes','1000')
obj1.Display()




