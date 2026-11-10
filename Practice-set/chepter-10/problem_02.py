# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.


class Calculator :
     
    def __init__(self , n):
        self.n = n
     
    def square(self):
        sq = self.n*self.n
        print("Square is : ",sq)
        
    def cube(self) :
        cb = self.n**3
        print("Cube is : ",cb)
        
    def squreRoot (self):
        sqr = self.n**0.5
        print("Squre Root is : ",sqr)
        
x = int(input("Enter the given number : "))

result = Calculator(x)

result.square()
result.cube()
result.squreRoot()