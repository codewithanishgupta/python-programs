''' 2. Write a program to fill in a letter template given below with name and date.
letter =
Dear <|Name|>,
You are selected!
<|Date|>
'''

# name = input("Enter the given name : ")

# date = input("Enter the given date : ")

# print(f"""
# Dear <|{name}>|,
# Your are selected!
# <|{date}|>
# """)

# using replace method

letter ='''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("Name","Anish Gupta").replace("Date","19 sep"))