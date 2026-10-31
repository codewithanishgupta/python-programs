'''26.	Write a program to calculate a student's total and average marks. 
Input:
•	5 subject marks 
Output:
Total Marks = ?
Average Marks = ?'''



marks1 = int(input("Enter 1st student marks : "))
marks2 = int(input("Enter 2nd student marks : "))
marks3 = int(input("Enter 3rd student marks : "))
marks4 = int(input("Enter 4th student marks : "))
marks5 = int(input("Enter 5th student marks : "))


total = marks1 + marks2 + marks3 + marks4 + marks5 

avarage = total/5

print("Total marks is : ",total)
print("Avarage marks is : ",avarage)