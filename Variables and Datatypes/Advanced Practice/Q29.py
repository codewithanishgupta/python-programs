''' 29.	Take the following input from the user: 
Name
Age
Basic Salary
Bonus
Calculate and display the total salary.'''


name = input("Enter user name ")
age = int(input("Enter usre age : "))
basic_salary = float(input("Enter user basic salary : "))
bonus = float(input("Enter user bonus : "))

total_salary = basic_salary + bonus

print("======= User Details =======")

print(f"Name : {name} \n Age : {age} \n Total salary : {total_salary}")