from PIL import Image, ImageOps
import sys
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[2].endswith(".jpg") and not sys.argv[2].endswith(".jepg") and not sys.argv[2].endswith(".png"):
        sys.exit("Invalid output")
    if os.path.splitext(sys.argv[2])[1] != os.path.splitext(sys.argv[1])[1]:
        sys.exit("Input and output have different extensions")
    try:
        img_file = sys.argv[1]
        img_person = Image.open(img_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


    img_shirt = Image.open("shirt.png")



    size = img_shirt.size
    img_person_fitted = ImageOps.fit(img_person, size)
    img_person_fitted.paste(img_shirt,img_shirt)
    img_person_fitted.save(sys.argv[2])



if __name__ == "__main__":
    main()
