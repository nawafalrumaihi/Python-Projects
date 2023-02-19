#
# def factorial(num: int) -> int:
#     """Return n! (0! is 1.)"""
#     if num <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, num + 1):
#         result *= x
#
#     return result
#
#
# for i in range(36):
#     print(i, factorial(i))
#

def factorial(num: int) -> int:
    """Returns the factorial of n!"""

    if num <= 1:
        return 1

    result = 2
    for i in range(3, num + 1):
        result *= i

    return result


for j in range(36):
    print(j, factorial(j))