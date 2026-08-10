# This program aims to calculate the total price of an order in a restaurant

MENU = {                   # Menu of the restaurant associating each item
    "Baja Taco": 4.25,     # with their prices
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def get_item() -> str:
    """Ask the user for an item. Returns None if the user interrupts the prompt
    with enter, ctrl+D or ctrl+C"""
    try:
        return input('Item: ').title()
    except (EOFError, KeyboardInterrupt):  # includes KeyboardInterrupt
        return None                             # to exit the program with Ctrl+C


def main() -> None:
    """Prints the total of the accumulated bill.
    The inputs conclude once Ctrl+D, Ctrl+C or enter is pressed"""
    total: float = 0.0
    while True:
        order = get_item()
        if not order:
            break
        if order in MENU:
            total = total + MENU[order]
            print(f'Total: ${total:.2f}')


if __name__ == '__main__':
    main()
