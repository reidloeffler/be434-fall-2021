#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-10-06
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence', metavar='str', help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    sequence = args.sequence
    out_file = args.outfile

    codon_table = {}
    codon = ''
    string_length = 0
    amino_acid = ''

    for line in args.codons:

        (line.rstrip().split())

        for track_char in range(5):

            if line[track_char] != ' ' and line[
                    track_char] != '\t' and track_char <= 3:
                codon += line[track_char]

            elif track_char == 4:
                codon_table[codon] = line[track_char]
                codon = ''

    while string_length in range(len(sequence) - 2):

        for track_char in range(3):

            codon += sequence[string_length]
            string_length += 1

        codon = codon.upper()

        if codon in codon_table:
            amino_acid += codon_table[codon]

        else:
            amino_acid += '-'

        codon = ''

    out_file.write(amino_acid)
    print('Output written to ' + '"' + out_file.name + '".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
