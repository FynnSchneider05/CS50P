def main():
    word = input("Input: ")
    shorten(word)


def shorten(word):
    vowels = "aeiouAEIOU"
    converted_text = ""

    for letter in word:
        if not letter in vowels:
            converted_text += letter
    return converted_text



if __name__ == "__main__":
    main()
