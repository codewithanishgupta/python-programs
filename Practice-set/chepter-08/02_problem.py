# 2. Write a python program using function to convert Celsius to Fahrenheit.


def fahrenheit(celsius = 0):
    return (celsius * 9/5)+32


print("in fahrenheight : ",fahrenheit(55))
print("in fahrenheight : ",fahrenheit(102))


def f_to_c (f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F : "))

c = f_to_c(f)

print(f"{round(c,2)}°C")