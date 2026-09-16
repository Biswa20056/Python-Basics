class SBI_Bank:
    location = 'marathalli'
    IFSC_Code = 'SBIN0001'
    ROi = 0.07
    def __init__(self,name,Aadhar,Acc_No,Balance):
        self.name = name
        self.Aadhar = Aadhar
        self.Acc_No = Acc_No
        self.balance = Balance
    def Check_Balance(self):
        print(f'The Available Balance is : {self.balance}')
    def deposit(self):
        account_No = int(input("Enter the Account Number : "))
        if self.Acc_No == account_No:
            amount = int(input("Enter the Amount to be deposited : "))
            if 500 <= amount <= 10000 and amount % 100 == 0:
                self.balance+=amount
                print('Credited Successfully!')
                print(f'The Available balance is : {self.balance}')
            else:
                print('Invalid Amount')
        else:
            print('Invalid Account Number')
    def Withdraw(self):
        amount  = int(input('Enter the amount : '))
        if 100 <= amount <= 20000 and amount % 100 == 0:
            if self.balance >= amount:
                self.balance -= amount
                print('Debitted Sussessfully!')
                print(f'The Available balance is : {self.balance}')
            else:
                print('Insufficient Balance')
        else:
            print('Invalid Amount')
cust1 = SBI_Bank('Biswajit',299701603155,987123,2300)
cust2 = SBI_Bank('SatyaPrashad',234090123786,345678,1200)
cust3 = SBI_Bank('Akash',200321450098,234000,4500)
print(cust1.name,cust1.Aadhar,cust1.Acc_No,cust1.balance)
cust2.name = 'Amit'
print(cust2.name)
SBI_Bank.Withdraw(cust1)