class SBI_Bank:
    location = 'Marathalli'
    IFSC_Code = 'SBIN00001'
    ROI = 0.07
    def __init__(self,name,Aadhar,Acc_No,Balance,pin):
        # here the below codes are for data saving
        self.name = name
        self.Aadhar = Aadhar
        self.Acc_No = Acc_No
        self.Balance = Balance
        self.pin = pin
    @classmethod# it will change the location for all the customers
    def change_loc(cls):
        cls.location = 'USA'
    @staticmethod
    def Get_Password():
        password = int(input("Enter the four digit pin : "))
        return password
    def Check_balance(self):
        count = 3
        while count > 0:
            print(f'Attempts Left {count}')
            if self.Get_Password() == self.pin:
                return f'Available Balance {self.Balance}'
            else:
                print('Incorrect Pin..')
                count-=1
        else:
            return f'No attempts left \nTry again after 24-hours'
    def deposit(self):
        count = 3
        while count > 0:
            print(f'Available attempts {count}')
            if self.Get_Password() == self.pin:
                amount = int(input("Enter the amount : "))
                if 100 <= amount <= 10000 and amount % 100 == 0:
                    self.Balance += amount
                    return f'Credited Successfully\nAvailable balance {self.Balance}'
                else:
                    print('Invalid Amount')
            else:
                print('Incorrect Pin')
                count -=1
        else:
            return f'No more attempts..\ntry again after 24-hours'
    def with_draw(self):
        count = 3
        while count > 0:
            print(f'Available attempts {count}')
            if self.Get_Password()==self.pin:
                amount = int(input('Enter the amount : '))
                if 100<=amount<=20000 and amount%100==0:
                    self.Balance-=amount
                    return f'Debitted Successfully\nAvailable balance {self.balance}'


cust1 = SBI_Bank('Biswa',299701602345,123456,800,1111)
cust2 = SBI_Bank('Raja',123456789987,234432234,-900,2222)
cust3 = SBI_Bank('Satya',1001001001,456789987,1000,3333)
print(cust1.deposit())