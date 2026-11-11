# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.


class Vector :
    def __init__(self , l):
        self.length = l
        
    def __len__(self):
        return len(self.length)
    
v1 = Vector([1,3,4])
print(len(v1))
v2 = Vector([1,3])
print(len(v2))