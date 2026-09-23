'''
Aquiring or imheriting the properties from single parent class to multiple child class is called hierarchical inheritance
'''
class Bank:
    def __init__(self,bal):
        self.bal = bal
    def Withdrawn(self):
        amount = int(input("Enter the Withdrwan amount : "))
        self.bal = self.bal - amount
        print('Withdrwan Suuessfully!')
        print(f'Available Balance : {self.bal}')
class PayTm(Bank):
    def __init__(self,bal):
        Bank.__init__(self,bal)
    def Withdrawn(self):
        Bank.Withdrawn(self)
class PhonePE(Bank):
    def __init__(self,bal):
        Bank.__init__(self,bal)
    def Withdrwan(self):
        Bank.Withdrawn(self)

cust1 = PhonePE(4000)
cust1.Withdrawn()