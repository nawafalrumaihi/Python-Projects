# open the .txt file to then be utilized throughout the script
with open('text.txt', encoding='utf-8', newline='') as sample:
    contents = sample.read()


def find_characters(text_sample):
    words = text_sample.split()
    for word in words:
        count = 0
        for char in word:
            if char == "A".casefold():
                count += 1
        print(f"the word - {word}: contains {count} a(s)")


find_characters(contents)
