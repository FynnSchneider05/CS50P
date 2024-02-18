import emoji as e


def main():
    text = input("Input: ")
    emoji = e.emojize(text, language="alias")
    print(emoji)


if __name__ == "__main__":
    main()
