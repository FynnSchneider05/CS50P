import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


    file = sys.argv[1]

    try:
        with open(file) as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            header = data[0]
            table = data
            table.remove(data[0])

            print(tabulate(table,header, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
