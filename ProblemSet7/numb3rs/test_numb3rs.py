from numb3rs import validate as v
from random import randint
def main():
    test_correct_ip()
    test_incorrect_ip()
    test_false_input()


def test_correct_ip():
    for i in range(0,100):
        n1 = randint(0,255)
        n2 = randint(0,255)
        n3 = randint(0,255)
        n4 = randint(0,255)
        assert v(f"{n1}.{n2}.{n3}.{n4}") == True

def test_incorrect_ip():

    for i in range(0,100):
        n1 = randint(0,255)
        n2 = randint(0,255)
        n3 = randint(0,255)
        n4 = randint(0,255)
        n5 = randint(256,1000)
        assert v(f"{n5}.{n2}.{n3}.{n4}") == False
        assert v(f"{n1}.{n5}.{n3}.{n4}")== False
        assert v(f"{n1}.{n2}.{n5}.{n4}")== False
        assert v(f"{n1}.{n2}.{n3}.{n5}")== False

        assert v(f"{n2}.{n3}.{n4}")== False
        assert v(f"{n1}.{n2}.{n3}.{n4}.{n1}")== False


def test_false_input():
    assert v("cat") == False
    assert v("hello") == False
    assert v("12-24-123-32") == False


if __name__ == "__main__":
    main()
