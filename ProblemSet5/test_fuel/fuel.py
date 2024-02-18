def main():
    fraction = input("Input: ")
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    parts = fraction.split("/")

    numerator = int(parts[0])
    denominator = int(parts[1])
    percent = round(numerator / denominator * 100)
    
    if percent > 100:
        raise ValueError

    return percent


def gauge(percentage):
    if percentage >= 99:
        return "F"
    if percentage <= 1:
         return "E"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
