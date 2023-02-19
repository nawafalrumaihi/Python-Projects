def custom_split(string, delimiter=' '):
    result = []
    start = 0
    for i, char in enumerate(string):
        if char == delimiter:
            result.append(string[start:i])
            start = i + 1
    result.append(string[start:])
    return result


text = "Good Morning Bahrain"
print(custom_split(text))

#Python 3+
name = input("who are you? ")
print("Suuuh duuude %s" % (name,))