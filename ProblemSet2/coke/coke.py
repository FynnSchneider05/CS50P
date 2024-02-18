def main():
    amount_owed = calculate()
    print("Change Owed: " + str(amount_owed))

def calculate():
    amount_left = 50
    amount_owed = 0

    while amount_left > 0:
        print("Amount Due: " + str(amount_left))
        inserted = int(input("Insert coin: "))
        if inserted == 5 or inserted == 10 or inserted == 25:
            amount_left -= inserted

    amount_owed = amount_left * -1
    return(amount_owed)



if __name__ == "__main__":
    main()
