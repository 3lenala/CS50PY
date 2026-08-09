def main():
    camel_case = input('camelCase: ')
    print(f'snake_case: {turn_to_snake_case(camel_case)}')

def turn_to_snake_case(camel_case: str) -> str:
    """Convert an identifier-like string to snake_case.

    Conversion rules:
    - Insert '_' before an uppercase letter that starts a new word.
    - Treat acronym to word transitions as word boundaries
      (for example, 'HTTPServer' -> 'http_server').
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
    - an uppercase letter follows a lowercase letter, or
    - an uppercase letter follows another uppercase letter and is followed
      by a lowercase letter, as in acronym-to-word transitions
      ('HTTPServer' -> 'http_server').
    """
    
    if index == 0 or not character.isupper():
        return False
    
    previous_char = camel_case[index-1]
    if previous_char.islower():
        return True 
    if index < len(camel_case) - 1:
        next_char = camel_case[index+1]
        if next_char.islower():
            return True
    return False
    

if __name__ == '__main__':
    main()