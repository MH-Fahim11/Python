grocery ={}

while True:
    try:
        items = input().upper()
        if items in grocery:
            grocery[items] += 1
        else:
            grocery[items] = 1
    except EOFError:
        print()
        break
for item, cou in sorted(grocery.items()):
    print(cou,item)