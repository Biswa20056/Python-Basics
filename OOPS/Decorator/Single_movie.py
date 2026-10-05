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

cust1 = Movie1()
cust1.Booking()
cust2 = Movie1()
cust2.Booking()