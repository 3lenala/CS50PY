# This program aims to, given a list of inputs given by the user, create an alphabetically
# sorted list of said items in uppercase with the number of times each has been introduced.


def get_items() -> dict[str, int]:
    """Prompts the user for the items and stores them as
    keys in a dictionary with the number of appearances as values"""
    items = {}
    while True:
        try:
            item = input().strip().upper()
        except (EOFError, KeyboardInterrupt):
            return items  # the input introduction is stopped when
            #  ctrl+D or ctrl+C are pressed
        if item == '':
            return items  # the input introduction ends when
            # enter is pressed
        if item in items:  # if the item has already been counted
            # update the count
            items[item] += 1
        else:
            items[item] = 1 # add element to the dictionary otherwise


def main() -> None:
    items = get_items()
    for item in sorted(items):
        print(f'{items[item]} {item}')


if __name__ == '__main__':
    main()
