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

cust1 = SBI_Bank('Biswa',299701602345,123456,800)
cust2 = SBI_Bank('Raja',123456789987,234432234,900)
cust3 = SBI_Bank('Satya',1001001001,456789987,1000)

# modifying incomon property by object reference
cust1.Aadhar = 12309090909
print(cust1.Aadhar)
print(cust2.Aadhar)