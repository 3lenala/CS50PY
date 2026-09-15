# This program aims to count how many lines of code a python file contains given the
# file as a command line argument. The command line argument should contain either the name
# of the file if it is contained in the same folder or the path to get to the file.

# A line is considered line of code when it is not empty and it is not a comment.

import sys

FILE_POSITION = 1
NUMBER_ARGS = 2


def get_file_path(args):
    """Get the name of the file located at FILE_POSITION.
    Raise Value Error if the given arguments do not meet the length or
    the extension criteria."""
    if len(args) < NUMBER_ARGS:
        raise ValueError('Too few command-line arguments')
    if len(args) > NUMBER_ARGS:
        raise ValueError('Too many command-line arguments')
    if not args[FILE_POSITION].endswith('.py'):
        raise ValueError('Not a Python file')
    return args[FILE_POSITION]


def is_code(line):
    """Verify if a given line is a code line or not."""
    stripped = line.strip()  # whitespaces or \n are not considered code.
    return (not stripped.startswith('#')) and stripped  # comments are not code.


def count_code_lines(file):
    """Count code lines inside a given file."""
    loc = 0
    for line in file:
        if is_code(line):
            loc += 1
    return loc


def main():
    """Retrieve name of python file, open the file and count the lines of code"""
    try:
        python_file = get_file_path(sys.argv)
    except ValueError as error:
        sys.exit(error)

    try:
        file = open(python_file)
    except FileNotFoundError:
        sys.exit('File does not exist')

    with file:
        print(count_code_lines(file))


if __name__ == '__main__':
    main()
