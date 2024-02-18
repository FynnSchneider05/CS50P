from twttr import shorten as s

def main():
    test_lowercase()
    test_uppercase()
    test_mixedcase()
    test_numbers()
    test_punctuations()

def test_lowercase():
    assert s("abcdefg") == "bcdfg"
    assert s("hello") == "hll"
    assert s("this is a test") == "ths s  tst"


def test_uppercase():
    assert s("ABCDEFG") == "BCDFG"
    assert s("HELLO") == "HLL"
    assert s("THIS IS A TEST") == "THS S  TST"

def test_mixedcase():
    assert s("aBcDeFg") == "BcDFg"
    assert s("HeLlO") == "HLl"
    assert s("ThIs Is A TeSt") == "Ths s  TSt"

def test_numbers():
    assert s("123") == "123"
    assert s("1a2B3I") == "12B3"

def test_punctuations():
    assert s("hello, world") == "hll, wrld"
    assert s("@.,A!§$%&/(B()=O?") == "@.,!§$%&/(B()=?"

if __name__ == "__main__":
    main()
