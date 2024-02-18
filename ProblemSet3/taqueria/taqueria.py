class NOMError(Exception):
    pass


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    price = 0
    while True:
        try:
            order = place_order()
            price += order
            print(f"Total: ${price:.2f}")

        except EOFError:
            print("")
            return

        except NOMError:
            continue

        else:
            continue


def place_order():
    order = input("Item: ").title()
    if order in menu:
        return round(menu[order], 2)

    else:
        raise NOMError("not on menu")


if __name__ == "__main__":
    main()
