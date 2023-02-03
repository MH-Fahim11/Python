li=[]
while True:
    try:
        name = input("Name: ")
        li.append(name)
    except EOFError:
        print()
        break
try:
    if len(li) == 1:
        print(f"Adieu, adieu, to {li[0]}")
    elif len(li) == 2:
        print(f"Adieu, adieu, to {li[0]} and {li[1]}")
    elif len(li) > 2:
        print("Adieu, adieu, to ", end="")
        for name in li:
            if name != li[-2]:
                print(f"{name}, ", end="")
            elif name == li[-2]:
                print(f"{name}, and {li[-1]}")
                break
except:
    pass