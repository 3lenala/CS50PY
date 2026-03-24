import math

MINUTES_IN_AN_HOUR = 60.0
HOURS_IN_A_DAY = 24.0
BREAKFAST_BEGINS = 7.0
BREAKFAST_ENDS = 8.0
LUNCH_BEGINS = 12.0
LUNCH_ENDS = 13.0
DINNER_BEGINS = 18.0
DINNER_ENDS = 19.0

def main() -> None:
    try:
        time_str = input('What time is it? ').strip()
        time_value = convert(time_str)
        meal_time = classify_time(time_value)
        if meal_time is not None:
            print(meal_time)

    except ValueError as exc:
        print(f"Error: {exc}")



def convert(time_str: str) -> float:
    """Convert a time string to decimal hours.

    Accepted formats:
    - "H" or "HH" (e.g., "7")
    - "HH:MM" (e.g., "7:30")
    - decimal hours (e.g., "7.5")

    Result given in decimal hours.
    """
    if not time_str:
        raise ValueError('Empty expression')
    if ':' in time_str:
        try: 
            hour_text, minute_text = time_str.split(":")
            hour_value = float(hour_text)
            minute_value = float(minute_text)
        except ValueError:
            raise ValueError('Invalid time input')
    else:   
        try:
            hour_value = float(time_str)
            minute_value = 0.0
        except ValueError:
            raise ValueError('Invalid time input')
    
    check_validity(hour_value, 'Hour', HOURS_IN_A_DAY)
    check_validity(minute_value, 'Minute', MINUTES_IN_AN_HOUR)

    return hour_value + minute_value / MINUTES_IN_AN_HOUR

def check_validity(value: float, name: str, upper_bound: float) -> None:
    """Validate that a numeric value is finite and within [0, upper_bound)."""  
    if not math.isfinite(value):
        raise ValueError(f'{name} must be finite.')
    if not (0 <= value < upper_bound):
        raise ValueError(f'{name} must be at least 0 and less than {upper_bound}.')

def classify_time(time_value: float) -> str | None:
    if BREAKFAST_BEGINS <= time_value <= BREAKFAST_ENDS:
        return 'breakfast time'
    if LUNCH_BEGINS <= time_value <= LUNCH_ENDS:
        return 'lunch time'
    if DINNER_BEGINS <= time_value <= DINNER_ENDS:
        return 'dinner time'
    return None


if __name__ == "__main__":
    main()
