import random

def main():
    i = 0
    score = 10
    level = get_level()
    # For 10 time Iteration
    while i<10:
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        t = 0
        # finding the courrect answer
        while True:
            t += 1
            #promt user for answer for 3 time
            if t <= 3:
                try:
                    print(f"{x} + {y} = ",end="")
                    ans = int(input())
                    if ans == z:
                        break
                    else:
                        print("EEE")
                        pass
                except:
                    print("EEE")
                    pass
            # if user failed to put currect answer for 3 time
            else:
                print(f"{x} + {y} = {z}")
                score -=1
                break
        i += 1
    print(f"Score: {score}")
#for getting currect level
def get_level():
     while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                break
        except:
            pass
     return level
#generate possative integer
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()