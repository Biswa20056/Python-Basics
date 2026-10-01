def SingleTon(arg):
    l = []
    def Inner():
        if len(l)==0:
            obj = arg()
            l.append(obj)
        return l[0]
    return Inner
@SingleTon #SingleTon(Movie1)
class Movie1():
    def __init__(self):
        self.regular = 20
        self.premium = 40
        self.recliner = 20
        self.box = 20
    def Booking(self):

        print(f'The present number of tickets for regular seat : {self.regular}')
        print(f'The present number of tickets for Premium seat : {self.premium}')
        print(f'The present number of tickets for recliner seat : {self.recliner}')
        print(f'The present number of tickets for Box seat : {self.box}')
        print('Available seats\n:1)regular\n 2)premium\n 3)recliner\n 4)box')

        choice_seat = input("Enter the seat customer wants : ")
        if choice_seat=='regular':
            reqtic_regular = int(input("Enter the number of ticket for regular seat : "))
            if reqtic_regular > 0 and reqtic_regular <= 5:
                    if reqtic_regular <= self.regular:
                        self.regular -= reqtic_regular
                        print(f'Total amount paid for {reqtic_regular} : {reqtic_regular*500}')
                        print('Booking Done...!')
                    else:
                        print('Booking Closed')
            else:
                print('Invalid Ticket')

        elif choice_seat=='premium':
            reqtic_premium = int(input("Enter the number of tickets for premium seat :"))
            if reqtic_premium > 0 and reqtic_premium<=6:
                if reqtic_premium<=self.premium:
                    self.premium -= reqtic_premium
                    print(f'Total Amount paid for {reqtic_premium} premium tickets : {700*reqtic_premium}')
                    print('Booking Done..!')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Ticket')

        elif choice_seat=='recliner':
            reqtic_recliner = int(input("Enter the number of tickets for recliner : "))
            if reqtic_recliner > 0 and reqtic_recliner<=4:
                if reqtic_recliner<=self.recliner:
                    self.recliner -= reqtic_recliner
                    print(f'The Amount Paid for {reqtic_recliner} recliner seats : {reqtic_recliner*800}')
                    print('Booking Done...!')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Tickets')

        elif choice_seat=='Box':
            reqtic_box = int(input("Enter the number of tickets fro box seat :"))
            if reqtic_box > 0 and reqtic_box <= 2:
                if reqtic_box <= self.box:
                    self.box -= reqtic_box
                    print(f'The Amount paid for {reqtic_box} box seat : {reqtic_box*1000}')
                    print('Booking Done')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Ticket')
        else:
            print('The Entered seats are not available in this theatre..!')

@SingleTon # SingleTon(Movie2)
class Movie2():
    def __init__(self):
        self.regular = 30
        self.premium = 50
        self.recliner = 40
        self.box = 30
    def Booking(self):

        print(f'The Available tickets for regular : {self.regular}')
        print(f'The Availabe seats for premium : {self.premium}')
        print(f'The Available tickets for recliner : {self.recliner}')
        print(f'The Available seats for bos : {self.box}')
        print('The type of seats available\n 1)regular\n 2)premium\n 3)recliner\n 4)box')

        seat_choice = input("Enter the seats you want : ")
        if seat_choice=='regular':
            reqtic_regular = int(input("Enter the number of ticket for regular : "))
            if reqtic_regular > 0 and reqtic_regular <= 5:
                if reqtic_regular <= self.regular:
                    self.regular -= reqtic_regular
                    print(f'The Amount Paid for {reqtic_regular} regular seat : {reqtic_regular*500}')
                    print('Booking Done...!')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Ticket')

        elif seat_choice=='premium':
            reqtic_premium = int(input("Enter number of seats fro premium :"))
            if reqtic_premium > 0 and reqtic_premium <= 6:
                if reqtic_premium <= self.premium:
                    self.premium -= reqtic_premium
                    print(f'The Amount paid for {reqtic_premium} premium seats : {reqtic_premium*700}')
                    print('Booking Done..!')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Tickets')

        elif seat_choice=='recliner':
            reqtic_recliner = int(input("Enter number of seats fro recliner :"))
            if reqtic_recliner > 0 and reqtic_recliner <= 4:
                if reqtic_recliner <= self.recliner:
                    self.recliner -= reqtic_recliner
                    print(f'The Amount paid for {reqtic_recliner} recliner seats : {reqtic_recliner*700}')
                    print('Booking Done..!')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Tickets')

        elif seat_choice=='Box':
            reqtic_box = int(input("Enter number of seats fro box :"))
            if reqtic_box > 0 and reqtic_box<= 2:
                if reqtic_box <= self.box:
                    self.box -= reqtic_box
                    print(f'The Amount paid for {reqtic_box} box seats : {reqtic_box*700}')
                    print('Booking Done..!')
                else:
                    print('Booking Closed')
            else:
                print('Invalid Tickets')
        else:
            print('The seats are not available in this Theatre..!')


@SingleTon # SingleTon(Movie3)
class Movie3():
    def __init__(self):
        self.regular = 40
        self.premium = 60
        self.recliner = 50
        self.box = 50
    def Booking(self):
       print(f'The Availabe seats for regular seats : {self.regular}')
       print(f'The Availabe seats for premium seats : {self.premium}')
       print(f'The Availabe seats for recliner seats : {self.recliner}')
       print(f'The Availabe seats for box seats : {self.box}')
       print('The Availabe seat types\n 1)regular\n 2)premium\n 3)recliner\n 4)box')

       seat_choice = input("Enter the seat customer wants :")
       if seat_choice=='regular':
           reqtic_regular = int(input("Enter number of seats for regular : "))
           if reqtic_regular > 0 and reqtic_regular <= 5:
               if reqtic_regular <= self.regular:
                   self.regular -= reqtic_regular
                   print(f'The Amount paid for {reqtic_regular} regular seat : {reqtic_regular*500}')
                   print('Booking Done..!')
               else:
                   print('Booking Closed')
           else:
               print('Invalid Tickets')

       elif seat_choice == 'premium':
           reqtic_premium = int(input("Enter number of seats for premium : "))
           if reqtic_premium > 0 and reqtic_premium <= 6:
               if reqtic_premium <= self.premium:
                   self.premium -= reqtic_premium
                   print(f'The Amount Paid for {reqtic_premium} premium seat : {reqtic_premium*700}')
                   print('Booking Done..!')
               else:
                   print('Booking Closed')
           else:
               print('Invalid Ticket')

       elif seat_choice == 'recliner':
           reqtic_recliner = int(input('Enter number of seats for recliner : '))
           if reqtic_recliner > 0 and reqtic_recliner <= 4:
               if reqtic_recliner <= self.recliner:
                   self.recliner -= reqtic_recliner
                   print(f'The Amount paid for {reqtic_recliner} recliner seats : {reqtic_recliner*800}')
                   print('Booking Done..!')
               else:
                   print('Booking Closed')
           else:
               print('Invalid Tickets')

       elif seat_choice == 'Box':
           reqtic_box = int(input('Enter number of seats for box : '))
           if reqtic_box > 0 and reqtic_box<= 2:
                if reqtic_box <= self.box:
                    self.recliner -= reqtic_recliner
                    print(f'The Amount paid for {reqtic_box} box seats : {reqtic_box*1000}')
                    print('Booking Done..!')
                else:
                    print('Booking Done')
           else:
               print('Invalid Tickets')
       else:
           print('The seats are not availabe in this theatre')

def BMYSW():
    print('1) Movie1 \n2) Movie2 \n3) Movie3')
    choice = int(input("Enter your Choice = "))
    if choice == 1:
        cust = Movie1()
        cust.Booking()
    elif choice == 2:
        cust = Movie2()
        cust.Booking()
    elif choice == 3:
        cust = Movie3()
        cust.Booking()
    else:
        print('No Movie Available')
def PayTm():
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
cust2 = PayTm()