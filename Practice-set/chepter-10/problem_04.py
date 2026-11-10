# 4. Add a static method in problem 2, to greet the user with hello.


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
        
    @staticmethod
    def greet ():
        print("Hello there!")
        
x = int(input("Enter the given number : "))

result = Calculator(x)

result.greet()
result.square()
result.cube()
result.squreRoot()