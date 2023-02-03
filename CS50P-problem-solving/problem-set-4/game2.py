import random

def main():
    level = get_int("Level: ")
    com_guess= random.randint(1, level)
    while True:
        guess = get_int("Guess: ")
        if guess > com_guess:
            print("Too large!")
        elif guess < com_guess:
            print("Too small!")
        else:
            print("Just right!")
            break

def get_int(text):
    while True:
        try:
            n = int(input(text))
            if n > 0:
                break
        except:
            pass
    return n

main()