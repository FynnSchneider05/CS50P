def main():
    camel_case = input("camelCase: ")
    snake_case = convert_case(camel_case)
    print(snake_case)


def convert_case(camel_case):
    snake_case = ""
    for letter in camel_case:
        if letter.islower():
            snake_case += letter
            continue
        snake_case += "_"
        snake_case += letter.lower()

    return snake_case


if __name__ == "__main__":
    main()
