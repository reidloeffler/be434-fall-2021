#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-10-19
Purpose: Assignment 7
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequences',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.sequences
    outfile = args.outfile
    iupac_codes = {
        'R': 'AG',
        'Y': 'CT',
        'S': 'GC',
        'W': 'AT',
        'K': 'GT',
        'M': 'AC',
        'B': 'CGT',
        'D': 'AGT',
        'H': 'ACT',
        'V': 'ACG',
        'N': 'ACGT'
    }

    for line in inputs:
        for sequence in line.split():
            # Iterates over each sequece inputed

            print(sequence, end=' ', file=outfile)
            # Prints origional sequence

            for char in sequence:
                # Iterates over the characters in each sequence

                if char in iupac_codes:
                    print('[' + iupac_codes[char] + ']', end='', file=outfile)
                # Prints translated charaters

                else:
                    print(char, end='', file=outfile)
                # Prints characters that were not translated

            print('\n', end='', file=outfile)
            # Starts next sequence translation on a new line

    if outfile != sys.stdout:
        print('Done, see output in "' + outfile.name + '"')


# --------------------------------------------------

if __name__ == '__main__':
    main()
