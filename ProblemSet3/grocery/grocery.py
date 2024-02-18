def main():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            print("")
            break

    print_list(grocery_list)


def print_list(grocery_list):
    list_keys = sorted(list(grocery_list))

    for key in list_keys:
        print(f"{grocery_list[key]} {key}")


if __name__ == "__main__":
    main()
