def main():
    msg = input()
    convert(msg)

def convert(msg):
    try:
        m1 = msg.replace(":)","🙂")
        m2 = m1.replace(":(","🙁")
    except:
        m1 = msg.replace(":(","🙁")
        m2 = m1.replace(":)","🙂")
    print(m2)
main()