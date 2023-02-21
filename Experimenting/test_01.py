string_test1 = ''


def check_palindrome(txt):
    if txt == txt[::-1]:
        return "The string is a palindrome"
    else:
        return "The string is not a palindrome"


while string_test1 != "quit":
    print(check_palindrome(string_test1))
    string_test1 = input("Enter a string: ").casefold()
