#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-10-27
Purpose: Assignment 8
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        type=int,
                        metavar='int ',
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return parser.parse_args()


# --------------------------------------------------


def find_kmers(FILE, num_kmer):
    """Builds kmer string and adds it to the kmers list, for FILE1 or FILE2s"""

    kmers = []
    # Empty list for kmers from each file

    for line in FILE:
        for word in line.split():
            for word_char_num in range(len(word) - num_kmer + 1):
                kmer = ''
                for kmer_char_num in range(num_kmer):
                    kmer += word[kmer_char_num + word_char_num]
                kmers.append(kmer)

    return kmers


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    FILE1 = args.FILE1
    FILE2 = args.FILE2
    num_kmer = args.kmer
    # Variables obtrained from command line input

    kmers1 = find_kmers(FILE1, num_kmer)
    kmers2 = find_kmers(FILE2, num_kmer)

    common_kmers = set()
    # Empty set for common kmers

    for kmer in kmers1:
        if kmer in kmers2:
            common_kmers.add(kmer)
    # Builds a set containing kmers that are in kmers1 and kmers2

    for kmer in common_kmers:
        # Iterates over the kmers in common_kmers

        count1 = 0
        count2 = 0

        for kmer1 in kmers1:
            if kmer1 == kmer:
                count1 += 1
        # Counts the number of times the kmer is found in kmers1

        for kmer2 in kmers2:
            if kmer2 == kmer:
                count2 += 1
        # Counts the number of times the kmer is found in kmers2

        print(f'{kmer:10}{count1:6}{count2:6}')
        # Prints the kmer and number of occuarnces for kmers1 and kmers2


# --------------------------------------------------

if __name__ == '__main__':
    main()
