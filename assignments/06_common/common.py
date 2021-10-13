#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-10-12
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

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
    FILE1 = args.FILE1
    FILE2 = args.FILE2
    outfile = args.outfile
    # Variables from commandline arguments

    words1 = set()
    words2 = set()
    # Empty list for each file

    for line in FILE1:
        for word in line.split():
            words1.add(word)
    # Builds set containing all words from FILE1

    for line in FILE2:
        for word in line.split():
            words2.add(word)
    # Builds set containing all words from FILE2

    for word in words1:
        if word in words2:
            print(word, file=outfile)
    # Compares contents of words1 and words2 to print common words


# --------------------------------------------------
if __name__ == '__main__':
    main()
