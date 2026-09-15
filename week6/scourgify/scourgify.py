""" This program aims to split the name column in a csv file into two
    different columns one containing the first name and another containing the last name.
    The rest of the columns in the original file remain the same. """

import sys
import csv


NEW_FILE_POSITION = 2
OLD_FILE_POSITION = 1
NUMBER_ARGS = 3


def get_files_path(args):
    """Get the name of the file located at NEW_FILE_POSITION and at OLD_FILE_POSITION.
    Raise ValueError if the given arguments do not meet the length or
    the extension criteria."""
    if len(args) < NUMBER_ARGS:
        raise ValueError('Too few command-line arguments')
    if len(args) > NUMBER_ARGS:
        raise ValueError('Too many command-line arguments')
    if not args[NEW_FILE_POSITION].endswith('.csv') or not args[OLD_FILE_POSITION].endswith('.csv'):
        raise ValueError('Not a CSV file')
    return args[OLD_FILE_POSITION], args[NEW_FILE_POSITION]


def read_csv_rows(file):
    """Return the csv rows as a list of dictionaries mapping column names to values."""
    return list(csv.DictReader(file))


def load_csv_rows(file_path):
    """Return the rows of the csv file from the given path as a list of dictionaries
    which contain the values for each column.
    Raise ValueError if the file cannot be opened."""
    try:
        file = open(file_path, newline='')
    except OSError as error:
        # translate the OSError so main can handle every failure with one except
        raise ValueError('File does not exist') from error

    with file:
        return read_csv_rows(file)


def split_name(row):
    """Create a dictionary of the new row where the name column has been split into two."""
    last, first = row['name'].split(',')
    return {'first': first.strip(), 'last': last.strip(), 'house': row['house']}


def get_new_rows(old_rows):
    """Return a list of each row where the name column has been split into two."""
    return [split_name(row) for row in old_rows]


def write_file(file_path, rows):
    """Write the rows into a csv file at the given path.
    Raise ValueError if there are no rows or the file cannot be written."""
    if not rows:
        raise ValueError('No rows to write')
    try:
        file = open(file_path, 'w', newline='')
    except OSError as error:
        # translate the OSError so main can handle every failure with one except
        raise ValueError('Unable to write') from error

    with file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    """Get the paths for the old and new files, read the rows from the old file, split the name column
    into two columns: first and last, and write a file with the split columns."""
    try:
        old_file, new_file = get_files_path(sys.argv)
        old_rows = load_csv_rows(old_file)
        new_rows = get_new_rows(old_rows)
        write_file(new_file, new_rows)
    except ValueError as error: # unified error
        sys.exit(error)


if __name__ == '__main__':
    main()
