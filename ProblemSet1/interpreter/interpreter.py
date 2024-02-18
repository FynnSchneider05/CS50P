def main():
    expression = input("Expression: ").strip()
    calculate(expression)


def calculate(ex):
    splittedEx = ex.split(" ")
    splittedEx[0] = float(splittedEx[0])
    splittedEx[2] = float(splittedEx[2])

    if splittedEx[1] == "+":
        print(splittedEx[0] + splittedEx[2])

    elif splittedEx[1] == "-":
        print(splittedEx[0] - splittedEx[2])

    elif splittedEx[1] == "*":
        print(splittedEx[0] * splittedEx[2])

    elif splittedEx[1] == "/":
        print(splittedEx[0] / splittedEx[2])


if __name__ == "__main__":
    main()
