# 20.	Take an integer from the user and convert it into a float and string.



num = int(input("Enter the given integer : "))

print("Number is ",num)

f = float(num)
s = str(num)

print(f"After convert number is Float : {f} {type(f)} , String : {s,type(s)}")