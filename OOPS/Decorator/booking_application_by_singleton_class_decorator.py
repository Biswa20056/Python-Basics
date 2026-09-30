def SingleTon(arg):
    l = []
    def Inner():
        if len(l)==0:
            obj = arg()
            l.append(obj)
        return l[0]
    return Inner
@SingleTon
class Movie1():
    def __init__(self):
        self.tic = 100
    def Booking(self):
        print(f'The present number of tickets : {self.tic}')
        reqtic = int(input("Enter the number of ticket : "))
        if reqtic > 0 and reqtic <= 10:
            if reqtic <= self.tic:
                self.tic = self.tic - reqtic
                print('Booking Done...!')
            else:
                print('Bookin Completed')
        else:
            print('Invalid Ticket')

@SingleTon
class Movie2():
    def __init__(self):
        self.tic = 150
    def Booking(self):
        print(f'The present number of tickets : {self.tic}')
        reqtic = int(input("Enter the number of ticket : "))
        if reqtic > 0 and reqtic <= 10:
            if reqtic <= self.tic:
                self.tic = self.tic - reqtic
                print('Booking Done...!')
            else:
                print('Bookin Completed')
        else:
            print('Invalid Ticket')

@SingleTon
class Movie3():
    def __init__(self):
        self.tic = 200
    def Booking(self):
        print(f'The present number of tickets : {self.tic}')
        reqtic = int(input("Enter the number of ticket : "))
        if reqtic > 0 and reqtic <= 10:
            if reqtic <= self.tic:
                self.tic = self.tic - reqtic
                print('Booking Done...!')
            else:
                print('Bookin Completed')
        else:
            print('Invalid Ticket')

def BMYSW():
    print('1) Movie1 \n2) Movie2 \n3) Movie3')
    choice = int(input("Enter your Choice = "))
    if choice == 1:
        cust = Movie1()
        cust.Booking()
    elif choice == 2:
        cust = Movie2()
        cust.Booking()
    elif choice ==3:
        cust = Movie3()
        cust.Booking()
    else:
        print('No Movie Available')

cust1 = BMYSW()
cust2 = BMYSW()
cust3 = BMYSW()

