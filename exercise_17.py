def fizz_buzz(num: int) -> int:
    """
    Plays the Game Fizz Buzz
    :param num: Checks to see if the number is divisible by either 3 which results in the return of "FIZZ" OR
        checks to see if the number is divisible by 5 which results in the return of "Buzz"
        But can also check that if the number is divisible both by 3 and 5 returns Fizz Buzz Combined
    :return: Either Fizz, Buzz, or Both contingent on the rules of the game
    """
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

    return num


for i in range(1, 101):
    fizz_buzz(i)

# error code 1: The issue is that the if-elif structure means that if the first condition is met,
# then the others won't be executed. To fix this, you should add the check for both conditions before
# the first two conditions.
