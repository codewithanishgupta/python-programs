# 2. Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ. Add a method ‘barkʼ to class ‘Dogʼ.

class Animal :
    def eat(self):
        return"eatting...."

class Pets(Animal):
    def name(self):
        return"Seru..."
        
class Dog (Pets):
    def bark(self):
        print(f"{self.name()} is barking And {self.eat()}")
        
d = Dog()
d.bark()

'''
class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.bark()
'''
