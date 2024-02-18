import fuel
import pytest


def main():
    test_convert_errors()
    test_convert()
    test_gauge()


def test_convert_errors():
    with pytest.raises(ValueError):
        assert fuel.convert("x/4")
        assert fuel.convert("x/h")
        assert fuel.convert("3/x")
        assert fuel.convert("10/4")

    with pytest.raises(ZeroDivisionError):
        assert fuel.convert("5/0")
        assert fuel.convert("20/0")

def test_convert():
    assert fuel.convert("1/1000") == 0
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/1") == 100
    assert fuel.convert("15/16") == 94
    assert fuel.convert("1/3") == 33

def test_gauge():
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(94) == "94%"
    assert fuel.gauge(1) == "E"

if __name__ == "__main__":
    main()
