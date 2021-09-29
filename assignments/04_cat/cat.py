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

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    files = args.file_input
    optional_num = args.number

    for num_files, file_info in enumerate(files):
        text = files[num_files].read()
        file_name = FileIO(file_info.name)
        num_lines = 1

        for num_characters, characters in enumerate(text):

            if text[num_characters - 1] == '\n' or num_characters == 0:

                if optional_num is True:
                    print('     ', end='')
                    print(num_lines, end='\t')

                print(characters, end='')
                num_lines += 1

            else:
                print(characters, end='')

        file_name.close()


# --------------------------------------------------

if __name__ == '__main__':
    main()
