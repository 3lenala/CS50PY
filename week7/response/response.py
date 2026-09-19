"""Verify the validity of a given email address."""

import validators


def main():
    """Prompt an email address and print whether it is valid or not."""
    print(check_validity(input("What's your email address? ")))


def check_validity(email: str) -> str:
    """Return 'Valid' if the inputted string has the structure of a valid email.
    Return 'Invalid' otherwise."""
    if validators.email(email):
        return 'Valid'
    return 'Invalid'


if __name__ == '__main__':
    main()
