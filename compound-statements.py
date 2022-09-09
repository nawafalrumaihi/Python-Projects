import datetime
import keyword

# Compound statements: contain (groups of) other statements; they affect or control the execution
# of those other statements in some way

# The compound statement includes the conditional and loop statement

#   if statement: it is a control flow statement that will execute statements under it if the condition is true.

#   while statements: the while loop statement repeatedly executes a code block while a particular condition is true

#   for statement: Using for loop statement, we can iterate any sequence or iterable variable. The sequence can be a:
#   string, list, dictionary, set, or tuple

#   try statement: specifies exception handlers

#   with statement: used to clean-up code for a group of statements, while the with statement allows the execution
#   of initialization and finalization  code around a block of code.

# Define a function
# function accepts two numbers and returns their sum
def addition(num1, num2):
    return num1 + num2  # return the sum of two numbers


# result is the return value
result = addition(20, 30)
print(result)

print()



# get current datetime
now = datetime.datetime.now()
print(now)

print(keyword.kwlist)
help("keywords")

print(help('if'))