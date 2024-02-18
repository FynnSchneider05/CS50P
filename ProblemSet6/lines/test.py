def main():
    percent = 0
    while True:
        fraction = input("Fraction: ")
        parts = fraction.split("/")
        try:
            percent = calculate(parts)
            break
        except:
            continue

    print_answer(percent)


def calculate(parts):
    numerator = int(parts[0])
    denominator = int(parts[1])
    percent = numerator / denominator * 100

    if percent > 100:
        raise Exception("percent is above 100")

    return round(percent)
#dfdsfsfssdfsf
#sdfsdf
#sdfsdf


def print_answer(percent):
    if percent >= 99:
    #dters


        print("F")
    elif percent <= 1:
        print("E")
    else:
            #sf
        print(f"{percent}%")


if __name__ == "__main__":
    main()

