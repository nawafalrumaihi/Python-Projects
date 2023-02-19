def multiply(x: float, y: float) -> float:
    """
    Multiplies two numbers.

    Although this function is intended to multiply two numbers, you can also use it
    to multiply a sequence. If you a pass a string, for example, as the first argument,
    you'll get the string repeated `y` times as the returned value.
    :param x: The first number to multiply
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


# word = input("Please enter a word or sentence to check if it is a palindrome: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

answer = multiply(18,3)
print(answer)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))


