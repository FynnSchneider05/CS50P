import jar as j
import pytest

def test_init():
    jar = j.Jar()

    assert(jar.size) == 0
    assert(jar.capacity) == 12


def test_init_invalid():
    with pytest.raises(ValueError):
        jar = j.Jar(-1)
        jar = j.Jar("cat")



def test_deposit():
    jar = j.Jar(10)
    jar.deposit(8)

    assert jar.size == 8

    assert jar.capacity == 10

    with pytest.raises(ValueError):
        assert jar.deposit(3)

def test_withdraw():
    jar = j.Jar(10)
    jar.deposit(8)

    jar.withdraw(5)

    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)


def test_str():
    jar = j.Jar(10)

    jar.deposit(8)

    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

    jar.withdraw(5)

    assert str(jar) == "🍪🍪🍪"

