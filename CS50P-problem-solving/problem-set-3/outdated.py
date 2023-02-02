month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()
    try:
        m,d,y = date.split("/")
        if int(m) >=1 and int(m) <= 12 and int(d) >=1 and int(d) <= 31:
            break
    except:
        try:
            om,od,y = date.split(" ")
            for i in range(len(month)):
                if om == month[i]:
                    m = i + 1
            if od.isnumeric() == False:
                d = od.replace(",","")
                if int(m) >=1 and int(m) <= 12 and int(d) >=1 and int(d) <= 31:
                    break
        except:
            pass
print(f"{y}-{int(m):02}-{int(d):02}")