import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if re.match(r"^[A-Z][A-Z]+([1-9][0-9]+)?$", s) and len(s) >= 2 and len(s) <= 6:
        return True

    return False


main()
