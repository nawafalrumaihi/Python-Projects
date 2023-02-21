def sum_numbers(*args: float) -> float:
    """
    Calculates the sum of all numbers passed as its arguments
    :param args:
    :return: The sum of all the numbers as a `float` stored in `result`
    """
    result = 0
    for i in args:
        result += i
        print(result)
    return result


user_input = float(input(f'Please enter a number: '))
sum_numbers(user_input)