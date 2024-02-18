import csv
import sys

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    try:
        converted_data = open_file()
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    write_file(converted_data)

def open_file():
    firsts = []
    lasts = []
    houses = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "name":
                continue
            last, first = row[0].strip("'").split(",")
            firsts.append(first)
            lasts.append(last)
            houses.append(row[1])
    data = {
        "firsts": firsts, "lasts": lasts, "houses": houses
    }
    return data

def write_file(data):
    firsts = data["firsts"]
    lasts = data["lasts"]
    houses = data["houses"]

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})

        for _ in range(0, len(firsts)):
            writer.writerow({"first": firsts[_].lstrip(), "last": lasts[_], "house":houses[_]})


if __name__ == "__main__":
    main()
