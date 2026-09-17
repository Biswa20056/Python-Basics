class SBI_Bank:
    loc = 'Marathalli'
    IFSC_No = 'SBIN0001'
    ROI = 0.07
    @classmethod
    def change_loc(cls):
        cls.loc = 'White-field'
        print(f'The current Location of the bank is {cls.loc}')
    @staticmethod
    def Get_password():
        password = int(input("Enter the Pin : "))
        return password
    def __init__(self,name,Phone_No,Aadhar_no,Acc_No,Balance,pin):
        self.name = name
        self.Phone_No = Phone_No
        self.Aadhar_No = Aadhar_no
        self.Acc_No = Acc_No
        self.Balance = Balance
        self.pin = pin
    def Check_Balance(self):
        count = 3
        while count > 0:
            print(f'The Available attempts are {count}')
            if self.Get_password() == self.pin:
                print(f'The Available Balance is {self.Balance}')
                break
            else:
                count -=1
                print(f'incorrect Pin..')
                print(f'{count} attempts left!')
        else:
            print(f'No attempts left..')
            print(f'Try again after 24-hours')
    def deposit(self):
        count = 3
        while count > 0:
            print(f'The Available Attempts are {count}')
            if self.Get_password() == self.pin:
                amount = int(input("Enter the amount to be deposited : "))
                if 500 <= amount <= 10000 and amount % 100 == 0:
                    self.Balance += amount
                    print('Credited Successfully!')
                    print(f'The Available Balance is {self.Balance}')
                    break
                else:
                    print('Invalid Amount')
                    print('Try Again..')
            else:
                count -= 1 
                print(f'{count} attempts left..')
                print('Invalid Pin')
                print('Try Again..')
        else:
            print('No more Attempts left..')
            print('Try Again after 24-hours..')
    def withdraw(self):
        count = 3
        while count > 0:
            print(f'The Available attempts {count}')
            if self.Get_password() == self.pin:
                amount = int(input("Enter the amount to be debitted : "))
                if self.amount >= amount:
                    if 100 <= amount <= 20000 and amount % 100 == 0:
                        self.Balance -= amount
                        print('Debitted Successfully!')
                        print(f'The Available Balance is : {self.Balance}')
                        break
                    else:
                        print('Invalid Amount')
                else:
                    print('Insufficient Balance')
            else:
                count -= 1
                print('Incorrect Pin')
                print(f'The Available attempts are {count}')
                print('Try Again..')
        else:
            print('No More attempts left!')
            print('Try again after 24-hours')

cust1 = SBI_Bank('Biswajit Nayak', 8260670660, 299701603155,12009, 3000,9889)
cust2 = SBI_Bank('Suman Patra', 8093256274, 888877774444, 8765, 4000, 2332)
cust3 = SBI_Bank('Santosh Padhiali', 7377084393, 222255551111, 1324, 9000, 5665)

cust2.Check_Balance()
