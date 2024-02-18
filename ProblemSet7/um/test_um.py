from um import count as c

def test_zero():
    assert c("yummy") == 0
    assert c("hello") == 0

def test_single_ums():
    assert c("hello um world") == 1
    assert c("hi, um my Name, um is Fynn") == 2

def test_ums_with_punctuations():
    assert c("um hello, um,") == 2
    assert c("um, Hi, my name um is Fynn um.") == 3
def test_upper_ums():
    assert c("Um hello, um,") == 2
    assert c("Um, Hi, my name um is Fynn um.") == 3
