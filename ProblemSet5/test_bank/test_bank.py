from bank import value

def main():
    test_hello()
    test_h()
    test_not_h()

def test_hello():
    assert value("hello") == 0
    assert value("Hello, world") == 0
    assert value("hello how are you?") == 0

def test_h():
    assert value("Hi, how are you?") == 20
    assert value("hallo") == 20

def test_not_h():
    assert value("moin") == 100
    assert value("Good morning") == 100



if __name__ == "__main__":
    main()
