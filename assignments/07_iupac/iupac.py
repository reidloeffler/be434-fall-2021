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
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'U': 'U',
        'T': 'T',
        'R': '[AG]',
        'Y': '[CT]',
        'S': '[GC]',
        'W': '[AT]',
        'K': '[GT]',
        'M': '[AC]',
        'B': '[CGT]',
        'D': '[AGT]',
        'H': '[ACT]',
        'V': '[ACG]',
        'N': '[ACGT]'
    }

    for sequence in inputs:
        # Iterates over each sequece inputed

        translation = ''.join([(iupac_codes.get(base, '-'))
                               for base in sequence])
        # Iterates over the characters in each sequence
        # Builds string containing seqence translation

        print(sequence, translation, file=outfile)
        # Prints sequence with translation

    if outfile != sys.stdout:
        print('Done, see output in "' + outfile.name + '"')
        # Prints output file name if not printing to stdout


# --------------------------------------------------

if __name__ == '__main__':
    main()
