def main():
    msg = input("Greeting:")
    usd = value(msg)
    print (f"${usd}")

def value(msg):
    text = msg.strip().lower()
    if text.startswith("h"):
        if "hello" in text:
            usd = 0
        else:
           usd = 20
    else:
        usd = 100
    return usd

if __name__ == "__main__":
    main()