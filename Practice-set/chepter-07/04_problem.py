# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enter the given number : "))

'''
count = 0
for i in range(1,n+1):
    if(n%i == 0):
        count +=1
        
if count == 2 :
    print("Given number is prime number!")
else:
    print("Given number is not a prime number!")
'''

# or next way

for i in range(2,n):
    if(n%i) == 0:
        print("Given number is not aprime number!")
        break
else:
    print("Given number is a prime number!")