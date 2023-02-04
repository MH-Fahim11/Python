from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()

def test_return_zero():
    assert value("hello") == 0
    assert value("hEllo") == 0
    assert value("HELLO") == 0
def test_return_20():
    assert value("hi") == 20
    assert value("hi gi") == 20
    assert value("HI ") == 20
def test_return_100():
    assert value("What's up!") == 100
    assert value("What's up! gi") == 100


if __name__ == "__main__":
    main()