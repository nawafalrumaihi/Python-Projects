import random


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: the String that the user will see, when
        they're promoted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        if temp != int:
            print("Please enter a number and try again!")


help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")


# my attempt at the challenge:
# while guess != answer:
#     print("Try again")
#     guess = int(input())
#
#     if guess > answer:
#         print("Try again")
#         guess = int(input())
#
#     if guess < answer:
#         print("Try again")
#         guess = int(input())
#
# if guess == answer:
#     print("Congratulatuons, you got it correct!")