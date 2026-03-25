def main():
    camel_case = input('camelCase: ')
    print(f'snake_case: {turn_to_snake_case(camel_case)}')

def turn_to_snake_case(camel_case: str) -> str:
    """Convert a camelCase string to snake_case."""
    snake_case_characters = []
    text_length = len(camel_case)
    previous_character = ''

    for index, character in enumerate(camel_case):

        if character.isupper():
            snake_case_characters.append(character.lower())
        elif character.islower():
            snake_case_characters.append(character)
        elif character.isnumeric():
            snake_case_characters.append(character)
        else:
            snake_case_characters.append('_')
        
        if index < (text_length - 1) and snake_case_characters:
            next_character = camel_case[index+1] 
            if word_transition(previous_character, character, next_character):
                snake_case_characters.append('_')
        previous_character = character

    return ''.join(snake_case_characters)

def word_transition(previous_character: str, character: str, next_character: str) -> bool:
    if character.isupper():
        if next_character.isnumeric() or (previous_character.isupper() and next_character.islower()):
            return True
    elif character.islower():
         if next_character.isupper() or next_character.isnumeric():
            return True
    elif  character.isnumeric():
        if next_character.isupper() or next_character.islower():
            return True
    return False


if __name__ == '__main__':
    main()