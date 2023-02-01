msg = input("What is the answer to the Great Question of Life, the Universe and Everything?")
if msg.strip() == "42":
    print("Yes")
elif msg.lower().strip() == "forty-two":
    print("Yes")
elif msg.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
