extensions = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}


def main():
    fileName = input("File name: ").lower().strip()
    printMediaType(fileName)


def printMediaType(fileName):
    if not "." in fileName:
        print("application/octet-stream")
        return

    splittedFileName = fileName.split(".")
    extension = splittedFileName[len(splittedFileName) - 1]

    if extension in extensions:
        print(extensions[extension])
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
