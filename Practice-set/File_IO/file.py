# file read
'''
f = open("text_file.txt")
r = f.read()
print(r)

f.close()
'''

# file write
'''
f = open("text_file.txt","w")

f.write("Anish is a good boy , he is smart ")

f.close()
'''

#file read in lines
'''
f = open("text.txt")
lines  = f.readlines()

print(lines,type(lines))
'''

# file read in line
'''
f = open("text.txt")

line1 = f.readline()
print(line1,type(line1))
line2 = f.readline()
print(line2,type(line2))
line3 = f.readline()
print(line3,type(line3))
line4 = f.readline()
print(line4,type(line4))
line5 = f.readline()
print(line5,type(line5))

line6 = f.readline()
print(line6 == "")
'''

# file append
'''
str = "This message is append to the text_file "
str2 = "This second message to verify"
f = open("text_file.txt","a")
f.write(str2)

f.close()
'''

#using with statement
f = open("text_file.txt")
print(f.read())
f.close()

# the same can be written using with statement like this : 
with open("text_file.txt") as f :
    print(f.read())

# you dont have to explicitly close the file 

