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
        description ='Solfege',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('lyrics',
                        metavar = 'str',
                        type = str,
                        nargs = '+',
                        help = 'Solfege')

    return parser.parse_args()

# --------------------------------------------------

def print_function(num_lyrics, lyrics):
    """ Print out associated lyrics """

    for count in range (num_lyrics):

        if lyrics[count] == 'Do':
            print ('Do, A deer, a female deer')
        if lyrics[count] == 'Re':
            print ('Re, A drop of golden sun')
        if lyrics[count] == 'Mi':
            print ('Mi, A name I call myself')
        if lyrics[count] == 'Fa':
            print ('Fa, A long long way to run')    
        if lyrics[count] == 'Sol':
            print ('Sol, A needle pulling thread')   
        if lyrics[count] == 'La':
            print ('La, A note to follow sol')           
        if lyrics[count] == 'Ti':
            print ('Ti, A drink with jam and bread')

        if lyrics[count] != 'Do'    \
       and lyrics[count] != 'Re'    \
       and lyrics[count] != 'Mi'    \
       and lyrics[count] != 'Fa'    \
       and lyrics[count] != 'Sol'   \
       and lyrics[count] != 'La'    \
       and lyrics[count] != 'Ti':
            print ('I don\'t know "' + lyrics[count] + '"')   

# --------------------------------------------------

def main():
    """ Make a jazz noise here """

    args = get_args()
    lyrics = args.lyrics
    num_lyrics = len (lyrics)

    print_function(num_lyrics, lyrics)

# --------------------------------------------------

if __name__ == '__main__':
    main()