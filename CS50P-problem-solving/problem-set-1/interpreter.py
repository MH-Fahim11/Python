expression = input("Expression:")

x, y, z = expression.split(" ")

if y =="+":
    result = float(x) + float(z)
elif y =="-":
    result = float(x) - float(z)
elif y =="*":
    result = float(x) * float(z)
elif y =="/":
    result = float(x) / float(z)
print(result)