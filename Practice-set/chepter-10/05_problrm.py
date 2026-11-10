from random import randint

class Train:
    def __init__(self , trainNo):
        self.trainNO = trainNo
    
    def book (self , fro , to):
        print(f"Ticket is booked in traion no {self.trainNO} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train no : {self.trainNO} is running on time")
        
    def getFare (self , fro , to ):
        print(f"Ticket fare in train no {self.trainNO} from {fro} to {to} is {randint(234,5555)}")
        
t = Train(2346)

t.book("panapur" , "Delhi")
t.getStatus()
t.getFare("Panapur" , "Delhi")