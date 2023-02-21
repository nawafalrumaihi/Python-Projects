import random

sorted_words = []
with open('nature.txt', encoding='utf-8', newline='') as list_of_words:
    for line in list_of_words:
        sorted_words.append(line.strip())


def encrypt_word(word: str):
    # Use a substitution cipher to encrypt the word
    # Replace all letters with underscores except for a few randomly chosen ones
    encrypted_word = ""
    for letter in word:
        if letter.isalpha():
            encrypted_word += "_" if random.random() < 0.7 else letter
        else:
            encrypted_word += letter
    return encrypted_word


def choose_random_word(word_shuffler: list):
    if len(word_shuffler) > 0:
        chosen_word = random.choice(word_shuffler).casefold()
        encrypted_word = encrypt_word(chosen_word)
        print("*" * 80)
        print(f"Chosen word: {encrypted_word}")
        print("*" * 80)
        num_guesses = 0
        while "_" in encrypted_word:
            guess = input("Guess a letter: ").casefold()
            if guess in chosen_word:
                for i, letter in enumerate(chosen_word):
                    if letter == guess:
                        encrypted_word = encrypted_word[:i] + guess + encrypted_word[i + 1:]
                print(f"Correct! {encrypted_word}")
            else:
                print("Incorrect!")
            num_guesses += 1
        print("*" * 80)
        print(f"Congratulations! You guessed the word in {num_guesses} guesses.")
    else:
        print("Sorry, try again")


choose_random_word(sorted_words)
