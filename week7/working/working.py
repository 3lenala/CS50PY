"""Convert a time range from 12-hour to 24-hour format.

Reads a range of the form "H:MM AM to H:MM PM" (minutes optional) from
standard input and prints its equivalent on a 24-hour clock."""
import re


FORMAT_12HOUR = fr'([1-9]|1[0-2])(?:\:([0-5][0-9]))? (A|P)M'
TIME_RANGE = fr'^{FORMAT_12HOUR} to {FORMAT_12HOUR}$'


def main():
    """Read a time range consisting of two 12-hour times separated by 'to'
    and print its equivalent in 24-hour format."""
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    """Convert the slice of string of time given in 12-hour format for its equivalent in 24-hour format.
    Raise ValueError if the input does not follow the patern given in SENTENCE."""
    if not re.search(pattern=TIME_RANGE, string=s):
        raise ValueError('Invalid Format')
    return re.sub(pattern=FORMAT_12HOUR, repl=change_format, string=s)


def change_format(match: re.Match) -> str:
    """Apply the format transformation on the hour and minutes. Return the string as HH:MM"""
    hour, minutes = apply_24_hour_format(match.group(1), match.group(2), match.group(3) == 'P')
    return f'{hour}:{minutes}'


def normalize(minutes: str) -> str:
    """Return minutes or '00' if no minutes were provided."""
    if minutes is None:
        return '00'
    return minutes


def pad_hour(hour: int) -> str:
    """Return the hour as a two digit string."""
    if hour < 10:
        return f'0{hour}'
    return f'{hour}'


def apply_24_hour_format(hour: str, minutes: str, post_meridiem: str) -> tuple[str, str]:
    """Convert a 12-hour time to its 24-hour representation"""
    hour = int(hour) % 12
    if post_meridiem:
        hour = hour + 12

    return pad_hour(hour), normalize(minutes)


if __name__ == "__main__":
    main()
