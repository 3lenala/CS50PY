# This program aims to calculate how many dollars to leave as a tip
# Given the price of the meal and the percentage of it the customer wants to leave


def main() -> None:
    try:
        dollars = dollars_to_float(input("How much was the meal? "))
        percent = percent_to_float(input("What percentage would you like to tip? "))
    except ValueError as exc:
        print(f"Error: {exc}")
        return
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """Convert a meal price string to a positive float."""
    try:
        dollars = float(d.replace('$','').strip())
    except ValueError:
        raise ValueError('Invalid meal price: must be numeric')
    
    if dollars <= 0:
        raise ValueError('Invalid meal price: must be strictly positive')
    return dollars

def percent_to_float(p: str) -> float:
    """Convert a percentage string to a decimal value."""
    try:
        percent = float(p.replace('%','').strip())
    except ValueError:
        raise ValueError('Invalid tip percentage: must be numeric')
    if percent > 100 or percent < 0:
        raise ValueError('Invalid percentage: must be between 0 and 100')
    return percent / 100

if __name__ == '__main__':
    main()
