SECRET_NUMBER = 42
game_is_over = False


def get_guess():
    guess = input("Guess the number: ")
    return guess


def is_int(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True


def end_game():
    global game_is_over
    game_is_over = True


def check_guess(guess):
    if (is_int(guess)):
        guess = int(guess)
        if (SECRET_NUMBER > guess):
            print(f"The secret number is greater than {guess}")
        elif (SECRET_NUMBER < guess):
            print(f"The secret number is less than {guess}")
        else:
            print(f"Congratulations, {guess} is the number!")
            end_game()
    else:
        if (guess == 'GIVE UP'):
            print("Game has been forfeited")
            end_game()
        else:
            print("Invalid input")


while (not game_is_over):
    guess = get_guess()
    check_guess(guess)
