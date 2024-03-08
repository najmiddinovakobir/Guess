import random

import color
from logo import logo

print(logo)
lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound, upper_bound)
print('''
|----------------------------|
|Name_of_level +    Attempts |
|--------------|-------------|
|Easy          |           10|
|Normal        |            7|
|Hard          |            4|
|Expert        |            2|
|Enter         |  Your choose|
------------------------------
''')
game_level = input("Enter the game level: ").lower()

max_attempts = 0
if game_level == 'easy':
    max_attempts = 10
    print("You choose easy level and You have 10 attempts")
elif game_level == 'normal':
    max_attempts = 7
    print("you have 7 attempts")
elif game_level == 'hard':
    max_attempts = 4
    print("you have a 4 attempts")
elif game_level == 'expert':
    print("You have a 2 attempts")
    max_attempts = 2
elif game_level == 'enter':
    enter_function = int(input("Enter number of attempts: "))
    max_attempts = enter_function
    print(f"You have {max_attempts} attempts")
else:
    print("Invalid Value")

if game_level in 'expert' or game_level in 'normal' or game_level in 'easy' or game_level in 'hard' or game_level in 'enter':
    def get_guess():
        while True:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(f"{color.LIGHT_RED}Invalid input. Please enter a number within the specified range.{color.END}")


    def check_guess(guess, number_secret):
        if guess == number_secret:
            return "Correct"
        elif guess < number_secret:
            return f"{color.BROWN}Too low{color.END}"
        else:
            return f"{color.LIGHT_GREEN}Too high{color.END}"


    def play_game():
        attempts = 0
        won = False

        while attempts < max_attempts:
            attempts += 1
            guess = get_guess()
            result = check_guess(guess, secret_number)

            if result == "Correct":
                print(f"{color.LIGHT_BLUE}You guessed the secret number {secret_number} in {attempts} attempts.{color.END}")
                won = True
                break
            else:
                print(f"{color.PURPLE}{result}. Try again!{color.END}")
                print(f"{color.LIGHT_RED}You have {max_attempts - attempts} attempts{color.END}")
        if not won:
            print(f"{color.YELLOW}Sorry, you ran out of attempts! The secret number is {secret_number}{color.END}.")


    play_game()
else:
    print("Goodbye!")