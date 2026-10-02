# 5. Write a program to find the sum of first n natural numbers using while loop


n = int(input("Enter the number : "))

sum = 0 

while (n>0):
    sum +=n
    n = n-1
    
print("Sum of n natural number is : ",sum)