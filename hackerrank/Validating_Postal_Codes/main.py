import re
regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

def main(P):
    res = (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
    return res

if __name__ == "__main__":
    postal_code = '110000'
    print(main(postal_code))

