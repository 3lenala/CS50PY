def main(): 
    camel_case = input('camelCase: ') 
    print(f'snake_case: {turn_to_snake_case(camel_case)}') 

def turn_to_snake_case(camel_case: str) -> str: 
    """Convert a camelCase string to snake_case.""" 
    snake_case_characters = [] 
    for character in camel_case: 
        if character.islower(): 
            snake_case_characters.append(character) 
        else: 
            if snake_case_characters: 
                snake_case_characters.append('_')
            snake_case_characters.append(character.lower()) 
            
    return ''.join(snake_case_characters) 

if __name__ == '__main__': 
    main()