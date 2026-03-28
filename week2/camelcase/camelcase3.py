def main():
    camel_case = input('camelCase: ')
    print(f'snake_case: {turn_to_snake_case(camel_case)}')

def turn_to_snake_case(camel_case: str) -> str:
    """Convert an identifier-like string to snake_case.

    Conversion rules:
    - Insert '_' before an uppercase letter that starts a new word.
    - Don't treat acronym to word transitions as word boundaries
      (e.g., 'HTTPServer' -> 'httpserver').
    - Normalize consecutive non-alphanumeric characters to a single '_'.
    - Remove the last '_' if the input ends with separators.
    - Keep digits attached to the surrounding word
      (for example, 'user2Name' -> 'user2_name').
    """
    
    if camel_case == '':
        return ''
    
    snake_case_characters = []

    for index, character in enumerate(camel_case):
        if character.isalnum():
            if word_transition(camel_case, index, character):
                snake_case_characters.append('_')
            snake_case_characters.append(character.lower())
        else:
            if snake_case_characters and snake_case_characters[-1] != '_':
                snake_case_characters.append('_')
    if snake_case_characters:
        if snake_case_characters[-1] == '_':
            snake_case_characters.pop(-1)

    return ''.join(snake_case_characters)

def word_transition(camel_case: str, index: int, character: str) -> bool:
    """Return True when the current uppercase character starts a new word.

    A new word starts when:
    - a lowercase letter follows an upperscase letter
    - a numeric character follows an uppercase letter
    """
    
    if index == 0 or not character.isupper():
        return False
    
    previous_char = camel_case[index-1]
    if previous_char.islower() or previous_char.isnumeric():
        return True 
    return False
    

if __name__ == '__main__':
    main()