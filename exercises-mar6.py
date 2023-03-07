"""
Write a function that takes two lists as input and
returns a new list containing only the elements that are common to both lists.
"""


def find_common(user_array1: list, user_array2: list) -> list:
    common_list = []
    for i in range(len(user_array1)):
        for j in range(len(user_array2)):
            if user_array1[i] == user_array2[j]:
                common_list.append(user_array1[i])

    return common_list


user_input1 = input("Enter a list of numbers, separated by commas: ")
user_input2 = input("Enter the second list of numbers, also separated by commas: ")

user_input1 = [int(num) for num in user_input1.split(',')]
user_input2 = [int(num) for num in user_input2.split(',')]

print("The common numbers you entered are: ")
print(find_common(user_input1, user_input2))
