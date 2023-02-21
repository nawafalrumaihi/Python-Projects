# code exercises to improve learning:

# exercise 1: write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

def find_fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


for i in range(1, 101):
    print(find_fizz_buzz(i))


# exercise 2: write a program that asks the user for a string and then prints out the length of the string
def find_length(string):
    return len(string)


user_input = input("Enter a string: ")
print(find_length(user_input))


# exercise 3: write a program that takes in a list of numbers and outs the sum of the numbers:
def sum_list(lis):
    summ = 0
    for nums in lis:
        summ += nums
    return summ


list_test = [1, 2, 3, 4, 5]
print(list_test)
print(sum_list(list_test))


# exercise 4: write a program that takes in a list of numbers and outputs the largest number in the the list and
# outputs all the even numbers in the original list:
def find_largest(lis):
    largest = 0
    for i in lis:
        if i > largest:
            largest = i
    return largest


list_test = [1, 2, 3, 4, 5]
print(list_test)
print(find_largest(list_test))

