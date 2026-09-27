# single line comment in python

'''Multiple line comment
    in python programing'''

# print in python

print("Hellow Python Program")

# Variable and datatypes in python
a=2
b=3.5
c=56.778866885
d=True
e="Anish Gupta"
print("\033[1;33m Type of data a is : ",type(a))
print("\033[1;34m Type of data b is : ",type(b))
print("\033[1;35m Type of data c is : ",type(c))
print("\033[1;36m Type of data d is : ",type(d))
print("\033[1;37m Type of data e is : ",type(e))


# input in python
a=int(input("Enter the given number : "))
print("Given number is : ",a)

name=str(input("Enter your name : "))
print("Welcome",name)

# conditional statement
# use of if
age =18
if age > 18 :
    print("Adult")

# use of if-else
if age > 18 :
    print("Adult")
else :
    print("Not Adult")

# use of nested if-else

x=23
y=78
z=56

if(x>y):
    if(x>z):
        print("Max : ",x)
    else:
        print("Max : ",z)
else:
    if(y>z):
        print("Max : ",y)
    else:
        print("Max : ",z)

# use of elif

if(x>y and x>z):
    print("Max : ",x)
elif(y>x and y>z):
    print("Max : ",y)
else:
    print("Max : ",z)
    