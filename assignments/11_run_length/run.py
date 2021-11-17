#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-11-16
Purpose: Assignment 11
"""

import argparse
import os

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('user_input',
                        metavar='str',
                        type=str,
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------


def check_input(user_input):
    """ Checks if the user provided a file or a sequence """

    if os.path.isfile(user_input):
        input_type = 'file'
    else:
        input_type = 'sequence'

    return input_type


# --------------------------------------------------


def build_output(sequence):
    """ Creates a compressed sequence """

    count = 1
    prev_char = ''
    output = ''

    for char in sequence:
        if char == prev_char:
            count += 1
        else:
            output += prev_char
            if count != 1:
                output += str(count)
            count = 1
        prev_char = char

    return output


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    user_input = args.user_input
    input_type = check_input(user_input)

    if input_type == 'sequence':
        sequence = user_input + ' '
        print(build_output(sequence))

    if input_type == 'file':
        sequences = open(user_input, 'rt', encoding='UTF-8')
        for sequence in list(sequences):
            print(build_output(sequence))


# --------------------------------------------------
if __name__ == '__main__':
    main()
