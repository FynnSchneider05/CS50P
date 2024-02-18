def main():
    text = input("Input: ")
    converted_text = convert(text)
    print("Output: " + converted_text)

def convert(text):
    vowels = "aeiouAEIOU"
    converted_text = ""

    for letter in text:
        if not letter in vowels:
            converted_text += letter
    return converted_text


if __name__ == "__main__":
    main()
