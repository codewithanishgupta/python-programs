''''
30.	🚀 Challenge Question 
Take a student's information:
Name
Roll Number
Age
5 Subject Marks
Height
Is Passed
Store every value using the appropriate Python data type and display a formatted student report containing:
========== STUDENT REPORT ==========

Name:
Roll Number:
Age:
Height:

Subject 1:
Subject 2:
Subject 3:
Subject 4:
Subject 5:

Total:
Average:
Passed:

'''

name = input("Enter student name : ")
roll_num = int(input("Enter student roll number : "))
age = int(input("Enter student age : "))
height = float(input("Enter student height (in fit) : "))

marks1,marks2,marks3,marks4,marks5 = map(int,input("Enter student 5 subject marks : ").split())

is_passed = True

total = marks1 + marks2 + marks3 + marks4 + marks5
average = total/5

is_passed = average >= 33

print("\n ========== Student Report ==========")
print(f"\nName : {name} \nRoll Number : {roll_num}\nAge : {age} \nHeight : {height}")

print(f"\nSubject1 : {marks1} \nSubject2 : {marks2} \nSubject3 : {marks3} \nSubject4 : {marks4} \nSubject5 : {marks5}")

print(f"\nTotal : {total} \nAvarage : {average} \nis_passed : {is_passed}")






