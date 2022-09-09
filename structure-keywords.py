# structure keywords: def, class, with, as pass, lambda

# the def keyword is used to define user-defined function or methods of a class

# def keyword: create function

## def addition(num1, num2):
#    print('Sum is', num1 + num2)

# call function
# addition(10,20)

# pass keyword: used to define as a placeholder when a statement is required syntactically
# code to add in future

### def sub(num1, num2):
###   pass

# class keyword: used to define class in Python. Object-orientated programing is a programming paradigm based on
# the concepts of "objects." An object-orientated paradigm is to design the program using classes and objects

# create class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# create object
s = Student('Jessa', 19)
s1 = Student('Ahmed', 20)

# call method
s.show()
s1.show()

# ******** #

# Variable Handling Keywords: del, global, nonlocal

#   the del keyword: used to delete the object

#   the global keyword: used to declare the global variable. Accessible anywhere in the code file

#   nonlocal variables are used in nested functions whose local scope is not defined. This means that the
#   variable can neither be in the local nor the global scope.
print("******")
price = 900 # global variable

def test1():
    print('price in 1st function :', price) #900

def test2():
    print("price in 2nd function :", price) #900

#call functions
test1()
test2()

#delete variable
del price
print("******")

