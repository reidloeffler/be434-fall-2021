#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-11-09
Purpose: Assignment 10
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'input_file',
        type=argparse.FileType('rt'),
        metavar='FILE',
        help='Input file',
    )

    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    input_file = args.input_file
    # Variables corresponding to command line input

    sequences = dict(enumerate(input_file))
    # Dictionary containing sequences from the input file
    ref_chars = dict(enumerate(sequences.get(1)))
    # Dictionary containing  reference characters for comparison
    seq_length = len(sequences.get(1))
    # Length of the sequences
    output = list(' ' * seq_length)
    # Output string with length that corresponds to the length of the sequences

    for sequence in sequences.values():
        # Iterates over all sequences

        chars = dict(enumerate(sequence))
        # Dictionary containing characters for comparison

        for num, char in chars.items():
            # Iterates over characters in the sequence

            for ref_num, ref_char in ref_chars.items():
                # Iterates over characters in the reference sequence

                if num == ref_num:
                    # Identifies corresponding characters by position

                    if char == '\n' and ref_char == '\n':
                        output[num] = ''
                    elif char == ref_char and output[num] != 'X':
                        output[num] = '|'
                    else:
                        output[num] = 'X'
                    # Compares corresponding characters
                    # Identifies overlapping characters
                    # Builds output string

    print(''.join(sequences.values()), end='')
    print(''.join(output))
    # Prints the sequences and output string


# --------------------------------------------------
if __name__ == '__main__':
    main()
