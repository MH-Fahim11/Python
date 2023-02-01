msg = input("Greeting:")
text = msg.strip().lower()
if text.startswith("h"):
    if "hello" in text:
        print("$0")
    else:
        print("$20")
else:
    print("$100")