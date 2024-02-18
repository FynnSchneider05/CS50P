import validators as val

def main():
    email = input("Enter email: ")
    print(validate_email(email))


def validate_email(e):
    if val.email(e):
        status = "Valid"
    else:
        status = "Invalid"

    return status
if __name__ == "__main__":
    main()
