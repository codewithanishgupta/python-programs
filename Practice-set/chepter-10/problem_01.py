# Create a class “Programmer” for storing information of few programmers working at Microsoft.


class Programmer :
    company = "Microsoft"
    
    def __init__(self,name , salary , id):
        self.name = name
        self.salary = salary
        self.id = id
    

a = Programmer("Anish",2300000,1)
print(a.name ,a.salary , a.id)

s = Programmer("sujeet",430000,34)
print(s.name ,s.salary , s.id)

