# This program aims to remove the vowels of an inputted string
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def main() -> None:
    input_text = input('Input text: ')
    print(f'Output text: {remove_vowels(input_text)}')

def remove_vowels(input_text: str) -> str:
    """Return the input string with all vowels removed."""
    no_vowel_characters = []
    for character in input_text:
        if character.lower() not in VOWELS:
            no_vowel_characters.append(character)
    return ''.join(no_vowel_characters)

if __name__ == '__main__':
    main()
