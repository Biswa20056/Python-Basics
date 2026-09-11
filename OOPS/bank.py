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
        
        # the part after self in the left side of equal operator is the variable name where the data which passed by the customer is saved
        # and that variable we can assign any type of variable name but we can not change the part in the right side of the equal sign

cust1 = SBI_Bank('Biswa',299701602345,123456,800)
cust2 = SBI_Bank('Raja',123456789987,234432234,900)
cust3 = SBI_Bank('Satya',1001001001,456789987,1000)

        
# access the uncommon property by instance reference
print(cust1.name,cust1.Aadhar,cust1.Acc_No,cust1.Balance)