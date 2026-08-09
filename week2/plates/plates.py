MAX_LENGTH = 6
MIN_LENGTH = 2


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate: str) -> bool:
    """Returns a boolean value indicating if the plate is valid or not. Vanity plates must:
    - Be between 2 and 6 characters long
    - Only include alphanumeric characters
    - Start with two letters
    - Not have 0 as the first digit
    - Not have numbers in the middle (numbers must go at the end)
   """

    length_plate = len(plate)
    if not (MIN_LENGTH <= length_plate <= MAX_LENGTH):
        return False
    
    if not plate.isalnum():
        return False
    
    if not plate[:2].isalpha():
        return False

    
    first_digit_index = find_first_digit(plate)
    if first_digit_index is not None:
        if plate[first_digit_index] == '0':
            return False
        
        if not plate[first_digit_index:].isdigit():
            return False
    return True

def find_first_digit(plate: str) -> int | None:
    for index, character in enumerate(plate):
        if character.isdigit():
            return index
    return None

if __name__ == '__main__':
    main()