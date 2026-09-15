# This program aims to print a formatted table of a given csv file using the tabulate module.

import sys
import csv
from tabulate import tabulate


FILE_POSITION = 1
NUMBER_ARGS = 2


def get_file_path(args):
    """Get the name of the file located at FILE_POSITION.
    Raise ValueError if the given arguments do not meet the length or
    the extension criteria."""
    if len(args) < NUMBER_ARGS:
        raise ValueError('Too few command-line arguments')
    if len(args) > NUMBER_ARGS:
        raise ValueError('Too many command-line arguments')
    if not args[FILE_POSITION].endswith('.csv'):
        raise ValueError('Not a CSV file')
    return args[FILE_POSITION]


def read_csv_rows(file):
    """Return the csv rows as a list of dictionaries mapping column names to values."""
    return list(csv.DictReader(file))


def format_table(raw_data):
    """Return the values as a formated table."""
    return tabulate(raw_data, headers="keys", tablefmt='grid')


def load_csv_rows(file_path):
    """Return the rows of the csv file from the given path as a list of dictionaries
    which contain the values for each column."""
    try:
        file = open(file_path, newline='')
    except OSError as error:
        raise ValueError('File does not exist') from error

    with file:
        return read_csv_rows(file)


def main():
    """Retrieve path of the csv file, open the file and print a table containing the information in the csv."""
    try:
        file_path = get_file_path(sys.argv)
        raw_data = load_csv_rows(file_path)
    except ValueError as error:
        sys.exit(error)
    print(format_table(raw_data))


if __name__ == '__main__':
    main()
