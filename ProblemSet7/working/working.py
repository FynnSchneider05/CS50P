import re
import sys

convertion_dic = {
    "12 AM": "00", "12 PM": "12"
}

def make_dicts():
    for i in range(1,12):
        convertion_dic[f"{i} AM"] = f"{i:02d}"
        convertion_dic[f"{i} PM"] = f"{i + 12}"


def main():
    print(convert(input("Hours: ")))



def convert_form_1(s):
    time_parts  = re.match(r"^([0-9]|1[0-2]) (AM|PM) to ([0-9]|1[0-2]) (AM|PM)$", s)
    hour1 = f"{time_parts.group(1)} {time_parts.group(2)}"
    hour2 = f"{time_parts.group(3)} {time_parts.group(4)}"
    time = f"{convertion_dic[hour1]}:00 to {convertion_dic[hour2]}:00"
    return time

def convert_form_2(s):
    time_parts = re.match(r"^([0-9]|1[0-2]):([0-5][0-9]|59) (AM|PM) to ([0-9]|1[0-2]):([0-5][0-9]|59) (AM|PM)",s)
    hour1 = f"{time_parts.group(1)} {time_parts.group(3)}"
    hour2 = f"{time_parts.group(4)} {time_parts.group(6)}"
    time = f"{convertion_dic[hour1]}:{time_parts.group(2)} to {convertion_dic[hour2]}:{time_parts.group(5)}"
    return time

def convert(s):
    if re.match(r"^(?:[0-9]|1[0-2]) (?:AM|PM) to (?:[0-9]|1[0-2]) (?:AM|PM)$", s):
        return convert_form_1(s)

    if re.match(r"^(?:[0-9]|1[0-2]):(?:[0-5][0-9]|59) (?:AM|PM) to (?:[0-9]|1[0-2]):(?:[0-5][0-9]|59) (?:AM|PM)",s):
        return convert_form_2(s)

    raise ValueError


make_dicts()


if __name__ == "__main__":
    main()
