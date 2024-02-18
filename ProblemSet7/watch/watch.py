import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if not re.search(r"src=\"https?://(www.)?youtube.com/embed(/[^\"]+)\"", s):
        print("None")
        sys.exit()

    url = re.search(r"src=\"(http)s?(://)(?:www.)?(youtu)(be).com/embed(/[^\"]+)\"", s)

    url = f"{url.group(1)}s{url.group(2)}{url.group(3)}.{url.group(4)}{url.group(5)}"

    return url

if __name__ == "__main__":
    main()

