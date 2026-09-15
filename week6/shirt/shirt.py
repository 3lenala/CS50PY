"""This program aims to overlay an image over another image given the file of the original picture,
and the file where the overlayed picture will be stored. They overlay image in the case by default is
an 'I took CS50' t-shirt."""

# FUTURE MODIFICATIONS: edge cases for the extension of a file.

import sys
from PIL import Image, ImageOps

INPUT_FILE_POSITION = 1
OUTPUT_FILE_POSITION = 2
NUMBER_ARGS = 3
FILE_NAME = 'shirt.png'
VALID_FORMATS = ['png', 'jpg', 'jpeg']


def get_extension(file_name):
    """Return the extension of a given file name."""
    return file_name.split('.')[-1].lower()


def validate_extensions(input_ext, output_ext):
    """Raise ValueError if the output extension does not meet the validity criteria
    or if the input and output extensions are not equal."""
    if output_ext not in VALID_FORMATS:
        raise ValueError('Invalid output')
    if output_ext != input_ext:
        raise ValueError('Input and output have different extensions')


def validate_number_args(len_args):
    """Raise ValueError if len_args does not equal NUMBER_ARGS global variable."""
    if len_args < NUMBER_ARGS:
        raise ValueError('Too few command-line arguments')
    if len_args > NUMBER_ARGS:
        raise ValueError('Too many command-line arguments')


def get_files_path(args):
    """Get the name of the file located at INPUT_FILE_POSITION and at OUTPUT_FILE_POSITION.
    Raise ValueError if the given arguments do not meet the length or
    the extension criteria."""
    validate_number_args(len(args))
    validate_extensions(get_extension(args[INPUT_FILE_POSITION]),
                        get_extension(args[OUTPUT_FILE_POSITION]))
    return args[INPUT_FILE_POSITION].lower(), args[OUTPUT_FILE_POSITION].lower()


def open_resize(file_name, size):
    """Open and resize image in input file."""
    try:
        image = Image.open(file_name)
    except OSError as error:
        raise ValueError('Input does not exist') from error
    image = ImageOps.fit(image, size)
    return image


def overlay_shirt(file_name, overlay=FILE_NAME):
    """Open image in file and paste the shirt image on top of it.
    Raise ValueError if the image cannot be opened."""
    try:
        over_image = Image.open(overlay)
    except OSError as error:
        raise ValueError('Overlay image does not exist') from error
    image = open_resize(file_name, over_image.size)
    image.paste(over_image, mask=over_image)
    return image


def save_image(image, file_name):
    """Save the image in file. Raise ValueError if the image cannot be saved."""
    try:
        image.save(file_name)
    except (ValueError, OSError) as error:
        raise ValueError('Unable to save output image') from error


def main():
    """Get the name of the before and after files. Put shirt on the before image.
    Save the image in the after file."""
    try:
        before, after = get_files_path(sys.argv)
        image = overlay_shirt(before)
        save_image(image, after)
    except ValueError as error:  # all the possible errors are unified in ValueError
        sys.exit(error)


if __name__ == '__main__':
    main()
