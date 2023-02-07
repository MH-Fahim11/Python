from twttr import shorten
def main():
    test_upper_lowwer()

def test_upper_lowwer():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"

def test_number():
    assert shorten("1234") == "1234"

def test_p():
    assert shorten("!,.") == "!,."

if __name__ == "__main__":
    main()