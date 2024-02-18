import requests
import sys

def main():
    price_one = get_data()
    amount = get_amount()
    price = price_one * amount
    price = f"${price:,.4f}"
    print(price)

def get_amount():
    if len(sys.argv) == 2:
        try:
            amount = float(sys.argv[1])
            return amount
        except:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing Command-line argument")

def get_data():
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    data = requests.get(api_url).json()
    price_one = float(data["bpi"]["USD"]["rate_float"])

    return price_one



if __name__ == "__main__":
    main()


