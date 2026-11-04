# Write a program to mine a log file and find out whether it contains ‘pythonʼ.

with open("log.txt") as f :
    content = f.read()
    
if "python" in content :
    print("Yes python is present!")
else:
    print("No python is not present!")