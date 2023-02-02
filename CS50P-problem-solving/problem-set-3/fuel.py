while True:
    try:
        text = input("Fraction:")
        x,y = text.split("/")
        f = (int(x) / int(y))
        if f <= 1:
           break
    except (ZeroDivisionError, ValueError):
        pass

p = f*100
if int(p) >= 99:
    print ("F")
elif int(p) <= 1:
    print("E")
else:
    print(round(p), end="")
    print("%")
