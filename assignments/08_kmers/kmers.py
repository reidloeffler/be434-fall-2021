#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-10-27
Purpose: Assignment 8
"""

import argparse
import sys


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
        parser.error(('--kmer "' +str(args.kmer) +'" must be > 0'))
    
    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    FILE1 = args.FILE1
    FILE2 = args.FILE2
    num_kmer = args.kmer
    # Variables from commandline arguments

    words1 = []
    words2 = []
    kmers = set()
    # Empty list for each file
    # Set for kners 

    for line in FILE1:
        for word in line.split():
            words1.append(word)
    # Builds list containing all words from FILE1

    for line in FILE2:
        for word in line.split():
            words2.append(word)
    # Builds list containing all words from FILE2

    for word in set(words1):
    # Iterates of the first set of words

        if word in set(words2):
        # Finds common words

            for word_char_num in range(len(word) - num_kmer+1):
            # Iterates over characters in common words

                kmer = ''
                count2 = 0

                for kmer_char_num in range(num_kmer):
                # Builds kner string 

                    kmer += word[kmer_char_num+word_char_num]
                
                word_char_num = kmer_char_num + word_char_num
                kmers.add(kmer)
    
    spaces = ''
    for _ in range(num_kmer, 13):
        spaces += ' '
    # For column spacing 
    
    for kmer in kmers:
        count1 = 0
        count2 = 0
        
        for word in words1:
            if kmer in word:
                count1 += 1
        
        for word in words2:
            if kmer in word:
                count2 += 1

        print(f'{kmer:10}{count1:6}{count2:6}')

# --------------------------------------------------

if __name__ == '__main__':
    main()
