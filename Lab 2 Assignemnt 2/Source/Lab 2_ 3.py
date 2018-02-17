# Airline Booking Reservation System
class Person: # creating 1st class person
    def __init__(self, a,b): # constructor for this class
        self._FName = a
        self._LName = b
        print('\n',"Name: ", self._FName, "", self._LName)

class Passenger (Person): # Inheritance, creating a 2nd class
    def __init__(self, g,h):# constructor for this class
        Person.__init__(self,g,h)

class Employee(Person): #Inheritance, creating a 3rd class
    def __init__(self, i,w):# constructor for this class
        Person.__init__(self, i,w)

class Booking: # creating a 4th class, which will determine the booking class of the courotmer
    __classlogic = '' # Private Data member
    def __init__(self,k): # constructor for this class
        Booking.classlogic=k
        self.bookingclass = ''
        if Booking.classlogic == 'e':
            self.bookingclass = 'Economy'
        elif Booking.classlogic == 'b':
            self.bookingclass = 'Business'
        print('\n','Your booking class is: ',self.bookingclass)

class seat: # creating a 5th class, assigning a set to the coustomer
    def __init__(self, q, r): # constructor for this class
        self.rownumber = q
        self.seatnumber = r
        print('\n', 'Your seat number is: ', self.rownumber," ", self.seatnumber)

class Booking_details(Passenger, Booking, seat): # Multiple Inheritance, Creating a 6th class
    def __init__(self,Fn,Ln,bclass,rnum,snum ): # constructor for this class
        print('\n', 'Thank you for booking with us, below are the detials for your reservations: ')
        Passenger.__init__(self,Fn,Ln) # super call constructor, instance for Passenger class
        Booking.__init__(self,bclass) # super call constructor, instance for booking class
        seat.__init__(self,rnum,snum) # super call constructor, instance for seat class




print('\n',"Welcome to Alfalah Booking site")
Uinput= input('For passenger please press p, for Employee press e, For visitor press v'  )
if Uinput =='p':
    F= input('Please Enter your first name: ')
    L= input('Please Enter your Last name: ')
    m = input("For booking a flight please press y: ")
    if m == 'y':
        n = input('Please select the booking class for economy press e, for business b')
    else:
        print('Your selection is invalid')
    t = input('To reserve your seat now please press y: ')
    if t == 'y':
        u= input('please enter the row number between 1 and 75: ')
        v = input('please enter a seat number between a and f: ')
    else:
        print('Your selection is invalid')

    p1= Booking_details(F,L,n,u,v) # super call is made here
elif Uinput == 'e':
    F = input('Please Enter your first name: ')
    L = input('Please Enter your Last name: ')
    print('Employee ', F, L, ',is being sucessfully logged into the system')
    e1=Employee(F,L)
elif Uinput == 'v':
    F = input('Please Enter your first name: ')
    L = input('Please Enter your Last name: ')
    print('Thank you for visitng our site ', F , L, ',please make sure you check our deals')
    v1=Person(F,L) # instance for Person class
else:
    print("Please make a valid selection")
