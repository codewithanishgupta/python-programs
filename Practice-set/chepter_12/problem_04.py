# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionErrorʼ .



try :
    a = int(input("Enter first integer : "))
    b = int(input("Enter second integer : "))
    result = a/b
    print(result)
except ZeroDivisionError as e :
    print("Infinite")
    