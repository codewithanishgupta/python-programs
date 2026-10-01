# 2. Write a program to find out whether a student has passed or failed if it requires a total of  40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter 1st sub marks :"))
marks2 = int(input("Enter 2nd sub marks :"))
marks3 = int(input("Enter 3rd sub marks :"))

total = marks1 + marks2 + marks3;

per = (total*100)/300

print("Total marks is : ",total)
print("Persentage is : ",per)

if (per >=40 and marks1 >=33 and marks2 >= 33 and marks3 >= 33):
    print("You are pass!")
else :
    print("yor are fail!")