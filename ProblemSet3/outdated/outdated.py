import re


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def main():
    while True:
        try:
            date = input("Date: ").strip()
            new_date = validate_date(date)
            break
        except:
            continue

    print(new_date)


def validate_date(date):
    if re.match(r"^([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[0-1])/[0-9]{4}$", date):
        return convert_form_one(date)

    parts = date.split(" ")
    if (
        parts[0] in months
        and re.match(r"^([1-9]|1[0-9]|2[0-9]|3[0-1]),$", parts[1])
        and re.match(r"[0-9]{4}$", parts[2])
    ):
        return convert_form_two(parts)

    else:
        raise Exception("Input not correct")


def convert_form_one(date):

    parts = date.split("/")

    year = f"{int(parts[2]) :04}"
    month = f"{ int(parts[0]) :02}"
    day = f"{int(parts[1]) :02}"

    new_date = f"{year}-{month}-{day}"

    return new_date


def convert_form_two(parts):

    year = f"{int(parts[2]):04}"
    month = f"{int(months[parts[0]]) :02}"
    day = parts[1].rstrip(",")
    day = f"{int(day):02}"

    if int(day) > 31:
        raise Exception("day > 31")

    new_date = f"{year}-{month}-{day}"
    return new_date


if __name__ == "__main__":
    main()
