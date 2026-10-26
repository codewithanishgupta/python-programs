''' 23.	Take two numbers as input from the user and print their: 
•	Sum 
•	Difference 
•	Multiplication 
•	Division 
'''

x,y = map(int,input("Enter two number : ").split())

print("Sum of given number : ", x+y)
print("Difference of given number : ", x-y)
print("Multiplication of given number : ", x*y)
print("Division of given number : ", x//y)