import random


def main():
    level = get_level()
    make_problems(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level != 3:
                raise ValueError
            break
        except:
            continue

    return level

def generate_integer(level):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)

def make_problems(level):
    score = 0
    for i in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)

        score += print_problems(x,y)
    print(f"Score: {score}")

def print_problems(x,y):
    for i in range(0,3):
        try:
            z = int(input(f"{x} + {y} = "))
        except:
            print("EEE")
            continue

        if z == x + y:
            return 1
        else:
            print("EEE")

    print(f"{x} + {y} = {x+y}")
    return 0



if __name__ == "__main__":
    main()
