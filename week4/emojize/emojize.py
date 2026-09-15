# This program aims to convert the codes (or aliases) introduced by the user to their corresponding emoji

import emoji


def main():
    """Converts the codes using emojize function from the emoji library"""
    user_input = input('Input: ')
    emojized = emoji.emojize(user_input, language='alias')
    print(f'Output: {emojized}')


if __name__ == '__main__':
    main()
