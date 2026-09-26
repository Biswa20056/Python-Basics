from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def CheckBal(self):
        pass# here developer should not give the implementation other wise th euse will get to know
class SBI_ATM(Bank):
    def CheckBal(self):
        print('Display balance')
class HDFC_ATM(Bank):
    def CheckBal(self):
        print("Display alance")

obj = SBI_ATM()
obj.CheckBal()
# we can not create instance for abstraction bcoz the implementation is incomple so creating object is useless
