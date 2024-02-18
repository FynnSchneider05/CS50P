import sys
import re


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not re.search(r"\.py$", sys.argv[1]):
        sys.exit("Not a Python file")

    try:
        lines_filtered = read_file()
        print(len(lines_filtered))

    except FileNotFoundError:
        sys.exit("File does not exist")


def read_file():
    lines_filtered = []
    with open(f"{sys.argv[1]}") as file:
        for line in file:
            if line.strip().startswith("#") or line.strip() == "":
                continue
            lines_filtered.append(line)

    return lines_filtered


if __name__ == "__main__":
    main()
