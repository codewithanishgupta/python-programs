# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector


class vector2:
    def __init__(self , x , y):
        self.x = x 
        self.y = y
    
    def display2D(self):
            print("x co-ordinate : ",self.x)
            print("y co-ordinate : ",self.y)
    
class vector3(vector2):
    def __init__(self, x, y , z):
        super().__init__(x, y)
        self.z = z
    
    def display3D(self):
        print("x co-ordinate : ",self.x)
        print("y co-ordinate : ",self.y)
        print("z co-ordinate : ",self.z)
        
        
v2 = vector2(10,23)
v2.display2D()

v3 = vector3(23,45,67)
# v3.display3D()
vector3.display3D(v3)