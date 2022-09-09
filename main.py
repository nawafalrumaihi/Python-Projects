# calculate area of rectangle:

# assinging two variables / statements in a single line of code
l = 10; b = 5

print ('Area of rectangle:', l * b)

###

#multi-line statements
addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70

print(addition)

#implicit continuation:
addition2 = (10 + 20 +
            30 + 40 +
            50 + 60 + 70)

print(addition2)

### we can also use square brackets [] to create a list. Then, if required, we can pleace
## each list item on a single line for better readability
# same as square brackets, we can also use curly to ceate a dictionary with every key-value pair

## list example:
names = ['Emma',
         'Kelly',
         'Jessa']

print(names)

# dictionary name as a key and mark as a value
# string:int

students = {'Emma': 70,
            'Kelly':65,
            'Jessa':75}

print(students)