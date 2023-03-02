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


def check_guess(guess):
    global game_is_over  # to access variable outside function

    if (is_int(guess)):
        guess_as_int = int(guess)
        if (SECRET_NUMBER > guess_as_int):
            print(f"The secret number is greater than {guess}")
            print("Try again!")
        elif (SECRET_NUMBER < guess_as_int):
            print(f"The secret number is less than {guess}")
            print("Try again!")
        else:
            print(f"Congratulations, {guess} is the number!")
            game_is_over = True
    else:
        if (guess == 'GIVE UP'):
            print("Game has been forfeited.")
            game_is_over = True
        else:
            print("Invalid input")
            print("Try again!")


while (not game_is_over):
    guess = get_guess()
    check_guess(guess)
