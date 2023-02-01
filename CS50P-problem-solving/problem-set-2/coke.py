print("Amount Due: 50")
due = 50
while True:
    coin = int(input("Insert Coin:"))
    if coin == 30:
        print("Amount Due: 50")
        continue
    else:
        due = due - coin
        if due > 0:
            print(f"Amount Due: {due}")
            continue
        if due == 0:
            print("Change Owed: 0")
            break
        if due < 0:
            print(f"Change Owed: {abs(due)}")
            break
