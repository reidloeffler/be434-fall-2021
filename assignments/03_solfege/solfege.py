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


# --------------------------------------------------A


def main():
    """ Make a jazz noise here """

    args = get_args()
    lyrics = args.lyrics
    num_lyrics = len(lyrics)

    outputs = dict(Do='Do, A deer, a female deer',
                   Re='Re, A drop of golden sun',
                   Mi='Mi, A name I call myself',
                   Fa='Fa, A long long way to run',
                   Sol='Sol, A needle pulling thread',
                   La='La, A note to follow sol',
                   Ti='Ti, A drink with jam and bread')

    for count in range(num_lyrics):

        if lyrics[count] in outputs:
            print(outputs[lyrics[count]])

        else:
            print('I don\'t know "' + lyrics[count] + '"')


# --------------------------------------------------

if __name__ == '__main__':
    main()
