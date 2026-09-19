"""Count number of 'um' words in a given sentence."""

import re


UM_PATTERN = r'\bum\b'


def main():
    """Prompt the user for an input and count the number of 'um' as independent words that appear in the input."""
    print(count(input('Text: ')))


def count(text: str) -> int:
    """Count number of appearances of the word 'um' in the input.
    For 'um' to be counted, it has to be between two word boundaries."""
    return len(re.findall(pattern=UM_PATTERN, string=text, flags=re.IGNORECASE))


if __name__ == '__main__':
    main()
