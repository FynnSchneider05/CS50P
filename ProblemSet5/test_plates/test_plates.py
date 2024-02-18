from plates import is_valid as v

def main():
    test_start()
    test_numbers()


def test_correct():
    assert v("AB124") == True
    assert v("ABDGT") == True
    assert v("KJF2") == True
    assert v("IKJ34") == True

def test_start():
    assert v("A1234") == False
    assert v("1234") == False
    assert v("2VH23") == False

def test_numbers():
    assert v("AB1AC") == False
    assert v("ABCD3A") == False
    assert v("A33B") == False
    assert v("124B") == False

def test_zero():
    assert v("ABAC0") == False
    assert v("ABCD03") == False
    assert v("KG0345") == False

def test_len():
    assert v("ADFGGR34") == False
    assert v("AHGRBVF") == False
    assert v("12357654") == False


def test_punctuation():
    assert v("AB.12") == False
    assert v("GD34!") == False
    assert v("_AG!") == False
    assert v("AHK,3") == False


if __name__ == "__main__":
    main()
