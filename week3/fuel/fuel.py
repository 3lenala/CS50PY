# This programs aims to return the percentage of fuel left given the fraction of fuel remaining inputted by the user.

EMPTY = 1     # Threshold for empty tank. Percentages at or below 1 are equivalent to an empty tank
FULL = 99     # Threshold for a full tank. Percentages at or above 99 are equivalent to a full tank


def get_fraction():
    """Prompts the user for a fraction until the dividend and divisor are integers.
    Considers Value Errors raised from converting said values to integers and from introducing
    a input that is not a fraction x/y."""
    while True:
        fraction_str = input('Fraction: ')
        try:
            x, y = fraction_str.split('/')
            x = int(x)
            y = int(y)
        except ValueError:
            continue
        if x < 0 or y < 0 or x > y:  # these cases do not raise an error but are nonetheless invalid inputs
            continue
        try:
            return x/y
        except ZeroDivisionError:
            continue


def remaining_fuel(fraction):
    """Returns the output string given the input fraction"""
    percentage = round(fraction * 100)
    if percentage <= EMPTY:
        return 'E'
    if percentage >= FULL:
        return 'F'
    return f'{percentage}%'


def main():
    """Given the inputted fraction, prints the percentage of fuel that is left."""
    fraction = get_fraction()
    print(remaining_fuel(fraction))


if __name__ == '__main__':
    main()
