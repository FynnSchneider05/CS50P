def main():
    text = input("Please enter any sentence here:  ")
    convertedText = convert(text)
    print(convertedText)


def convert(text):
    convertedText = text.replace(":)", "🙂").replace(":(", "🙁")
    return convertedText


if __name__ == "__main__":
    main()
