import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass
com_guess= random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > com_guess:
                print("Too large!")
            elif guess < com_guess:
                print("Too small!")
            else:
                print("Just right!")
                break
    except:
        pass