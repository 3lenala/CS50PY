# This program aims to print the number of calories a piece of fruit introduced by the user has according to the FDA's database
FILENAME = 'nutrition.txt'

from sys import exit

def get_dataset(filename: str) -> dict[str, int]:
    """Stores name of the item and calories from FILENAME dataset into a dictionary"""
    try:
        with open(filename) as file:
            data = {}
            for line in file:
                tokens = line.split()
                calories = int(tokens.pop()) #   tokens.pop() Returns tokens[-1] and removes it from the tokens list
                item = (' '.join(tokens)).lower() #   creates a string with the name of the item
                data[item] = calories
            return data
    except FileNotFoundError:
        exit(f'{filename} database not found')

def check_calories(data: dict[str, int], item: str) -> int | None:
    """Check whether the item is in the database, in which case it returns the item's calories.
    It returns None if the item is not in the database"""
    if item in data:
        return data[item]
    return None 

def main() -> None:
    """Given an item inputted from the user it returns the calories of one piece of such item according to
    the FDA's poster of fruits. The output is printed if the element exists in the database. 
    If the element is not in the database, it is ignored. """
    data = get_dataset(FILENAME)
    item = input('Item: ').lower()
    calories = check_calories(data=data, item=item)
    if calories is not None:
        print(calories)

if __name__ == '__main__':
    main()
