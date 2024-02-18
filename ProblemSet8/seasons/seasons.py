from datetime import date, timedelta
import inflect
import sys
import re

def main():
    born_date = test_input(input("Birthday (YYYY-MM-DD): "))

    today = date.today()

    print(calculate_difference(born_date, today))


def test_input(input):
    if re.match(r"^[0-9]{4}-(0[0-9]|1[0-2])-(0[0-9]|1[0-9]|2[0-9]|3[0-1])$", input):
        return input
    else:
        sys.exit("Wrong Input")


def calculate_difference(born_date, today):
    born_date = date.fromisoformat(born_date)

    if type(today) == str:
        today = date.fromisoformat(today)


    delta = today - born_date
    days = delta.days

    minutes = days * 24 * 60

    engine = inflect.engine()
    text = engine.number_to_words(int(minutes))
    text = text.replace("and ", "")
    return f"{text.capitalize()} minutes"


if __name__ == "__main__":
    main()
