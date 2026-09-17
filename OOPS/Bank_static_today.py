class SBI_Bank:
    location = 'Marathalli'
    IFSC_Code = 'SBIN00001'
    ROI = 0.07
    def __init__(self,name,Aadhar,Acc_No,Balance,password):
        # here the below codes are for data saving
        self.name = name
        self.Aadhar = Aadhar
        self.Acc_No = Acc_No
        self.Balance = Balance
        self.password = password
    @classmethod# it will change the location for all the customers
    def change_loc(cls):
        cls.location = 'USA'
    def Check_Balance(self):
        pin = int(input("Enter the Pin : "))
        if self.password==pin:
            print(f'Available Balance is : {self.Balance}')
        else:
            print('Invalid Pin')
    def with_draw(self):
        amount = int(input("Enter the with-drawn amount : "))
        if 100<= amount <= 20000 and amount%100==0:
            if self.Balance>=amount:
                self.Balance-=amount
                print('Amount with-drwan successfully')
                print(f'Available balance is {self.Balance}')
            else:
                print('Insufficient Balance')
        else:
            print('Invalid Amount')
    def Deposit(self):
        account_no = int(input("Enter the account_no : "))
        if self.Acc_No==account_no:
            amount = int(input('Enter the amount you want to deposit :'))
            if 500<=amount<=20000 and amount%100==0:
                self.Balance+=amount
                print('Deposite successful')
                print(f'Available balance : {self.Balance}')
            else:
                print('Invalid Amount')
        else:
            print('Invalid Account Number')


cust1 = SBI_Bank('Biswa',299701602345,123456,800,2222)
cust2 = SBI_Bank('Raja',123456789987,234432234,-900,1111)
cust3 = SBI_Bank('Satya',1001001001,456789987,1000,3333)
cust1.Check_Balance()
