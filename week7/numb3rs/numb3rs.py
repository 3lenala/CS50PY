# This program aims to validate an IP address.
# A valid IP address contains four numbers from 0 to 255 separated by dots.
# Each one of those numbers are called an octet.

import re

# Regular expression of a number between 0 and 255
OCTET = r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
# Regular expression of an IP adress
IP_REGEX = rf"{OCTET}(\.{OCTET}){{3}}"


def main():
    """Print True if the inputted string is a correct IPv4 address,
    print False otherwise."""
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validate the structure of the given IP address by comparing
    it to the regular expression of an IP address."""
    return bool(re.fullmatch(pattern=IP_REGEX, string=ip))


if __name__ == "__main__":
    main()
