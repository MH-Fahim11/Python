def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalpha() == True and len(s) >= 2 and len(s) <= 6:
        return True
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if s[(len(s)-2)].isalpha() == True:
        return False
    i=0
    while i < len(s):
        if s[i].isalpha() == False:
          if s[i] == "0":
              return False
          else:
                break
        i += 1
    for letter in s:
        if letter in [" ", "-", "_", ",", "?","."]:
            return False
    return True
main()