# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using ‘object.a = 0ʼ. Does this change the class attribute?


class Demo :
    a = 30
    

object = Demo ()
print(object.a) # print the class attribute because instance attribute is not present 

object.a = 0 ;

print(object.a)   # print the object attribute because instance attribute is  present

print(Demo.a) # class attribute print