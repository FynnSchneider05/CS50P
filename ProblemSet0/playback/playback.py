def main():
    sentence = input("Please enter any sentence here:  ")
    slowesSentence = replaceSpaces(sentence)
    print(slowesSentence)


def replaceSpaces(sentence):
    sentence = sentence.replace(" ", "...")
    return sentence


if __name__ == "__main__":
    main()
