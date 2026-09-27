# 2. Write a program to accept marks of 6 students and display them in a sorted manner


marks = []


print("Enter the 7 marks here  ")

for i in range(1,7):
    m=int(input(f"Enter {i} marks : "))
    marks.append(m)

print(marks)

print("In shorted sorter")
marks.sort()
print(marks)