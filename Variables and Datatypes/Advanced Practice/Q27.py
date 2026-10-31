'''
27.	Write a program to calculate a person's age in months and days from their age in years. 
Example:
Age = 20
Months = 240
Days = 7300

'''

year = int(input("Enter your age : "))

month = year * 12 
day = year*365

print("Your age in month : ",month)
print("your age in days : ",day)
