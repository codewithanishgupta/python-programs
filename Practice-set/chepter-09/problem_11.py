# . Write a python program to rename a file to “renamed_by_python.txt”.


with open("old.txt") as f:
    content = f.read()
    
with open("new.txt","w") as f :
    f.write(content)