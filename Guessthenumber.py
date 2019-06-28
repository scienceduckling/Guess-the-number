import random


def gameplay():
    """Guess the number game"""

    while True:
        try:
            upper_limit = int(input("Enter upper limit for interval you want to guess from. Low limit will be 1. It has to be whole number.: "))
        except ValueError:
            print("That's not a whole number. We will use 100 as upper limit.")
            upper_limit = 100

        number = random.randint(1, upper_limit + 1)
        guesses = 0
        print("Guess our whole number between 1 and {}".format(upper_limit))
        while True:
            try:
                player_guess = int(input("Enter your guess here: "))
                guesses = guesses + 1
                if player_guess == number:
                    print("Correct! You win!")
                    break
                elif player_guess > number:
                    print("Wrong! The answer is lower than that.")
                elif player_guess < number:
                    print("Wrong! The answer is higher than that.")
            except ValueError:
                print("That's not a whole number, try again.")
                continue
        print('You got it in', guesses, 'guesses!')

        play_again = str(input("Play again? (y/n): "))
        if play_again != 'y':
            break


if __name__ == "__main__":
    gameplay()
