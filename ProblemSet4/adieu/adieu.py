def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    message = genMessage(names)
    print(message)


def genMessage(names):
    message = "\nAdieu, adieu, to"

    if len(names) == 1:
        message += f" {names[0]}"
        return message

    if len(names) == 2:
        message += f" {names[0]} and {names[1]}"
        return message

    for name in names:

        if names.index(name) == len(names) - 1:
            message += f" and {name}"
            break

        message += f" {name},"

    return message


if __name__ == "__main__":
    main()
