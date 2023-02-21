# exercise 6: write a program that takes in a string and reverses the order of the words
def reverse_string(string):
    string_list = string.split()
    string_list.reverse()
    return ' '.join(string_list)


user_input = input("Enter a sentence: ")
print(reverse_string(user_input))
