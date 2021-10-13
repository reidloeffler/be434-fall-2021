#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-10-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=argparse.FileType('wt'),
        default="<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    FILE1 = args.FILE1
    FILE2 = args.FILE2
    # outfile = args.outfile

    common_words = []
    file1 = list(FILE1)
    file2 = list(FILE2)
    text1 = ''
    text2 = ''
    length1 = len(file1)
    length2 = len(file2)

    for i in range(length1):
        text1 += file1[i]

    for i in range(length2):
        text2 += file2[i]

    set1 = (text1.rstrip().split())
    set2 = (text2.rstrip().split())
    length3 = len(set1)

    for i in range(length3):
        if set1[i] in set2 and set1[i] not in common_words:
            common_words.append(set1[i])

    common_words = sorted(common_words)
    length4 = len(common_words)

    for i in range(length4):
        print(common_words[i])


# --------------------------------------------------
if __name__ == '__main__':
    main()
