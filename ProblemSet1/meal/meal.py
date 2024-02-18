def main():
    time = input("What time is it? ")
    convertedTime = convert(time)
    if convertedTime >= 7 and convertedTime <= 8:
        print("breakfast time")
    elif convertedTime >= 12 and convertedTime <= 13:
        print("lunch time")
    elif convertedTime >= 18 and convertedTime <= 19:
        print("dinner time")


def convert(time):
    parts = time.split(":")
    minutes = float(parts[1]) / 60
    convertedTime = float(parts[0]) + minutes
    return convertedTime


if __name__ == "__main__":
    main()
