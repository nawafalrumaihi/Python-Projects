import random

countries_and_capitals = {
    "Argentina": "Buenos Aires",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "China": "Beijing",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "Mexico": "Mexico City",
    "Russia": "Moscow",
    "South Africa": "Pretoria",
    "South Korea": "Seoul",
    "Turkey": "Ankara",
    "United Kingdom": "London",
    "United States": "Washington, D.C."
}

def play_game():
    score = 0
    number_of_questions = 10
    asked_capitals = set()
    for i in range(number_of_questions):
        capital = random.choice(list(countries_and_capitals.values()))
        while capital in asked_capitals:
            capital = random.choice(list(countries_and_capitals.values()))
        country = [k for k, v in countries_and_capitals.items() if v == capital][0]
        answer = input(f"What country has the capital {capital}: ")
        if answer == country.casefold():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {country}.")
        asked_capitals.add(capital)
    print(f"You got {score} out of {number_of_questions} questions correct.")

play_game()
