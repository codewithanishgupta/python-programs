# 6. Write a program to calculate the factorial of a given number using for loop.


n = int(input("Enter the given number : "))
fact = 1 ;

for i in range (1, n+1):
    fact = fact *i
    
print("Factorial of the given number is : ", fact)