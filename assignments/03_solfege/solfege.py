#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-09-22
Purpose: Solfege
"""

import argparse

# --------------------------------------------------


def get_args():

    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('lyrics',
                        metavar='str',
                        type=str,
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------


def print_function(num_lyrics, lyrics):
    """ Print out associated lyrics """

    for count in range(num_lyrics):

        i = 0

        while i == 0:

            if lyrics[count] == 'Do':
                print('Do, A deer, a female deer')
                i += 1
            if lyrics[count] == 'Re':
                print('Re, A drop of golden sun')
                i += 1
            if lyrics[count] == 'Mi':
                print('Mi, A name I call myself')
                i += 1
            if lyrics[count] == 'Fa':
                print('Fa, A long long way to run')
                i += 1
            if lyrics[count] == 'Sol':
                print('Sol, A needle pulling thread')
                i += 1
            if lyrics[count] == 'La':
                print('La, A note to follow sol')
                i += 1
            if lyrics[count] == 'Ti':
                print('Ti, A drink with jam and bread')
                i += 1
            if i == 0:
                print('I don\'t know "' + lyrics[count] + '"')
                i += 1


# --------------------------------------------------


def main():
    """ Make a jazz noise here """

    args = get_args()
    lyrics = args.lyrics
    num_lyrics = len(lyrics)

    print_function(num_lyrics, lyrics)


# --------------------------------------------------


if __name__ == '__main__':
    main()
