class SBI_Bank:
    location = 'Marathalli'
    IFSC_Code = 'SBIN00001'
    ROI = 0.07
    def __init__(self,name,Aadhar,Acc_No,Balance):
        # here the below codes are for data saving
        self.name = name
        self.Aadhar = Aadhar
        self.Acc_No = Acc_No
        self.Balance = Balance
    def Check_Balance(self):
        self.Balance = 1500

cust1 = SBI_Bank('Biswa',299701602345,123456,800)
cust2 = SBI_Bank('Raja',123456789987,234432234,-900)
cust3 = SBI_Bank('Satya',1001001001,456789987,1000)
print(cust1.Balance)
SBI_Bank.Check_Balance(cust2)
print(cust2.Balance)