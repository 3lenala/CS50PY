# This program aims to print the number of calories a piece of fruit introduced by the user has according to the FDA's database

DATA = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew melon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80,
    }


def main() -> None:
    """Given an item inputted from the user it returns the calories of one piece of such item according to
    the FDA's poster of fruits. The output is printed if the element exists in the database.
    If the element is not in the database, it is ignored. """

    item = input('Item: ').lower()
    if item in DATA:
        print(f'Calories: {DATA[item]}')


if __name__ == '__main__':
    main()
