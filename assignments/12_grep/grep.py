#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-11-23
Purpose: Assignment 12
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('search_term',
                        type=str,
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('input_files',
                        type=argparse.FileType('rt'),
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        action='store_true',
                        default=False,
                        help='Case-insensitive search')

    parser.add_argument('-o',
                        '--outfile',
                        type=argparse.FileType('wt'),
                        metavar='FILE',
                        default=sys.stdout,
                        help='Output')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    search_term = args.search_term
    input_files = args.input_files
    insensitive = args.insensitive
    outfile = args.outfile

    if '?' in search_term:
        search_term = search_term[:len(search_term) - 2]

    for file in input_files:
        for line in file:
            if search_term in line and insensitive is False:
                if len(input_files) > 1:
                    print(file.name + ':', end='', file=outfile)
                print(line, end='', file=outfile)
            elif (search_term.lower() in line.lower() and insensitive is True):
                if len(input_files) > 1:
                    print(file.name + ':', end='', file=outfile)
                print(line, end='', file=outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
