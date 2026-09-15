from enum import IntEnum
from typing import NamedTuple

class Index(IntEnum):
    MONTH = 0
    DAY = 1
    YEAR = 2
    
    
class Tokens(NamedTuple):
    month : str
    day : str
    year : str
  
    
class Month(NamedTuple):
    days : int
    name : str
    number : str   
    
    
class Months(NamedTuple):
    January : Month
    February : Month
    March : Month
    April : Month
    May : Month
    June : Month
    July : Month
    August : Month
    September : Month
    October : Month
    November : Month
    December : Month
   

MONTHS = {
    "January": Month("January", "01", 31),
    "February" : Month("February", "02", 28),
    "March" : Month("March", "03", 31),
    "April" : Month("April", "04", 30),
    "May" : Month("May", "05", 31),
    "June" : Month("June", "06", 30),
    "July" : Month("July", "07", 31),
    "August" : Month("August", "08", 31),
    "September" : Month("September", "09", 30),
    "October" : Month("October", "10", 31),
    "November" : Month("November", "11", 30),
    "December" : Month("December", "12", 31)
}

NUMBER_MONTHS = len(MONTHS)

EXPECTED_TOKENS = len(Index)


def get_date():
    while True:
        date_input = input('Date: ').strip()
        
        tokens = date_input.split('/')
        if len(tokens) != EXPECTED_TOKENS:
            tokens = date_input.split(' ')
            if len(tokens) != EXPECTED_TOKENS:
                continue
            try:
                month = MONTHS[tokens[Index.MONTH].title()]
            except KeyError:
                continue
            tokens[Index.MONTH] = month
            if not tokens[Index.DAY].endswith(','):
                continue
            tokens[Index.DAY] = tokens[Index.DAY].rstrip(',')
            
        try:
            date = {
                'day': correct_format(tokens[Index.DAY]),
                'month': correct_format(tokens[Index.MONTH]),
                'year': tokens[Index.YEAR]
            }
        except (ValueError, IndexError):
            continue
        
        if is_valid(date):
            return date

def correct_format(item):
    if (int(item) < 10):
        return f'0{int(item)}'
    return item

def is_valid(date):
    try:
        day = int(date['day'])
        month = int(date['month'])
    except ValueError:
        return False
    if not (0 < month <= NUMBER_MONTHS):
        return False
    try:
        max_days = MONTHS[date['month']].days
    except KeyError:
        return False
    return (0 < day <= max_days)


def main():
    date = get_date()
    print(f"{date['year']}-{date['month']}-{date['day']}")


if __name__ == '__main__':
    main()
