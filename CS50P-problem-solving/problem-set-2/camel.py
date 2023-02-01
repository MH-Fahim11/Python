camelCase = input("camelCase:")


print("snake_case:", end="")

for letter in camelCase:
    if letter.isupper():
        print("_", end="")
        print(letter.lower(), end="")
    else:
        print(letter, end="")
print()
