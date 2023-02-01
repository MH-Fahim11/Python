text = input("Input:")
word =""
for letter in text:
    if letter in ["a","e","i","o","u","A","E","I","O","U"]:
        continue
    else:
        word += letter
print("Output:",word)