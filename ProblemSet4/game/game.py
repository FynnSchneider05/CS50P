import random
import sys


class WrongGuessError(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
            break

        except ValueError:
            continue

    number = random.randint(1, level)

    while True:
        try:
            make_guess(number)

        except WrongGuessError as e:
            print(e)
            continue

        except ValueError:
            continue


def make_guess(number):
    guess = int(input("Guess: "))

    if guess == number:
        print("Just right!")
        sys.exit()
    elif guess < number:
        raise WrongGuessError("Too small!")
    elif guess > number:
        raise WrongGuessError("Too large!")


if __name__ == "__main__":
    main()
