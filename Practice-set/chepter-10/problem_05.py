# 5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways

class Train :
    seats = 20
    bookseat = 0
    fare = 450

    def bookTicket(self):
        if(self.bookseat < self.seats):
            self.bookseat +=1
            print("Seat book successfully!")
            
        else :
            print("No seats available!")
            
    def getStatus(self):
        print("No of seats available is : ",self.seats-self.bookseat)
        
    def information (self):
        
        if (self.bookseat > 0):
            print("Fare is Rs.", self.fare)
    
    
t = Train()

t.bookTicket()
t.getStatus()
t.information()