import random


def attempt(random_num):
    guess_count = 0
    guess = 0
    while guess != random_num:
        try:
            guess = int(input("Enter a guess:  "))
            guess_count += 1
        except ValueError:
            print("You entered an invalid value. Make sure it is a whole number")
            continue
        if guess < random_num:
            print("You guessed too low")
            continue
        elif guess > random_num:
            print("You guessed too high")
            continue
        else:
            break
    print("\nYou guessed correctly! The number was {}, and it took you {} guesses.".format(random_num, guess_count))
    print("The game is complete. Thanks for playing!")


def start_game():
    print("Welcome to my guessing game!")
    random_num = random.randint(1, 10)
    attempt(random_num)


start_game()
