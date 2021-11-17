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
        # Checks if the input corresponds to an existing file
        input_type = 'file'
    else:
        # Estblishes that the file is a sequence if it is not file
        input_type = 'sequence'

    return input_type
    # Returns the input type


# --------------------------------------------------


def build_output(sequence):
    """ Creates a compressed sequence """

    count = 1
    prev_char = ''
    output = ''

    for char in sequence:
        # Iterates over each character in the sequence

        if char == prev_char:
            count += 1
            # Counts the number of occurrences if character is repeated

        else:
            output += prev_char
            if count != 1:
                output += str(count)
            count = 1
            # Adds the previous character to the output string
            # Adds the number occurrences to the output string
            # Resets count to 1

        prev_char = char
        # Reassigns the previous character value to the current character

    return output
    # Returns the compressed sequence


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    user_input = args.user_input
    input_type = check_input(user_input)

    if input_type == 'sequence':
        # Checks if the input is a string/sequence

        sequence = user_input + ' '
        print(build_output(sequence))
        # Passes the string/sequence in to the build_ouput function
        # Prints compressed sequence

    if input_type == 'file':
        # Checks if the input corresponds to an existing file

        sequences = open(user_input, 'rt', encoding='UTF-8')
        for sequence in list(sequences):
            print(build_output(sequence))
        # Reads file line by line
        # Passes each line/sequence in to the build_ouput function
        # Prints compressed sequence for each line/sequence


# --------------------------------------------------
if __name__ == '__main__':
    main()
