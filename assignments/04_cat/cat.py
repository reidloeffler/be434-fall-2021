#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-09-28
Purpose: Rock the Casbah
"""

import argparse
from io import FileIO

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file_input',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')
    # Positional argument: obtains file handles

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default=False)
    # Optional boolean argument: allows the user to view
    # file contents with numbered lines

    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    files = args.file_input
    optional_num = args.number

    for num_files, file_info in enumerate(files):
        # For statment: Iterates over list containing input files

        num_line = 1
        text = files[num_files].read()
        file_name = FileIO(file_info.name)
        # Pulls name attribute from file_info and converts it to FileIO type

        for num_characters, characters in enumerate(text):
            # For statment: Iterates over list containing characters
            # for a given file

            if (optional_num is True and
                    (text[num_characters - 1] == '\n' or num_characters == 0)):
                # If statement: Determines if line numbers will be printed
                # based on user input

                alt_begining = '     ' + str(num_line) + '\t' + characters
                # Builds alterative beginning string for numbered lines
                print(alt_begining, end='')
                num_line += 1

            else:
                print(characters, end='')
                # Prints contents from file(s)

        file_name.close()
        # Closes files that were opened


# --------------------------------------------------

if __name__ == '__main__':
    main()
