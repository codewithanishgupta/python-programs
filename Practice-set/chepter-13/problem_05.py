# 5. Write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce

l = [23,34,34,3444,4445,64354,34545,4334]

def greater(a , b):
    if a > b :
        return a
    return b

print(reduce(greater , l))