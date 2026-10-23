# 1. Write a program using functions to find greatest of three numbers


def gretest(x=0,y=0,z=0):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
    
    
# function call
result = gretest(1452,34,61)
print("Greatest of three number is ",result)