# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

    # Text string
text = input("Please type in any word or sentence: ")

    # Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1

    # Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)

    # Why use a dictionary to store the letter frequencies, compared to a list or tuple?
    """
        A dictionary is used in this code because it provides a way to map unique 
        keys (in this case, the letters and digits in the input string) to values
        (in this case, their frequency/count) which allows for efficient lookups
        and updates on the count for each key.
        
        Using a tupple or list would not be a good choice in this case because there is no 
        natural order or index for the keys (letters and digits), and accessinf the count
        for a particular key would require searching through the entire list or tuple.
        
        A dictionary, on the other, provides constant-time access to the count for a particular key
        using its hash value, which makes it more appropriate data structure for this use case. 
    """