from working import convert as c
import pytest



def test_format_1():
    assert c("5 AM to 8 PM") == "05:00 to 20:00"
    assert c("5 PM to 8 AM") == "17:00 to 08:00"
    assert c("12 AM to 12 PM") == "00:00 to 12:00"

def test_format_2():
    assert c("5:00 AM to 8:20 PM") == "05:00 to 20:20"
    assert c("5:40 PM to 8:12 AM") == "17:40 to 08:12"
    assert c("12:12 AM to 12:42 PM") == "00:12 to 12:42"


def test_wrong_format():
    with pytest.raises(ValueError):
        c('9 AM - 9 PM')

def test_wrong_hour():
    with pytest.raises(ValueError):
        c('13 AM to 17 PM')

def test_wrong_minutes():
    with pytest.raises(ValueError):
        c('9:60 AM to 9:60 PM')
