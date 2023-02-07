def main():
    word = input("Input:")
    print("Output: " + shorten(word))

def shorten(word):
    text =""
    for letter in word:
        if letter.lower() in ["a","e","i","o","u"]:
            continue
        else:
            text += letter
    return text
if __name__ == "__main__":
    main()