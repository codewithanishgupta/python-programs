'''
25.	Write a program that takes a number as input and displays: 
Original value
Original data type
Converted float value
Converted float data type
Converted string value
Converted string data type
'''

num = int(input("Enter the given number : "))
print(f"Original value : {num} , Original data type : {type(num)}")

float_num = float(num) 
print(f"Converted Float value : {float_num} , Converted Float data type : {type(float_num)}")

str_num = str(num)
print(f"Converted String value : {str_num} , Converted String data type : {type(str_num)}")