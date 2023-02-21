# write a program that takes in a list of numbers and sorts them in ascending order

def sort_list(lis):
    lis.sort()
    return lis


user_input = input("Enter a list of numbers separated by commas: ")
user_input = user_input.split(',')
user_input = [int(i) for i in user_input]
print(sort_list(user_input))
