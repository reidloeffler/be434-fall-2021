#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-09-07
Purpose: Print greeting
"""

import argparse

# --------------------------------------------------

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greetings and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting ',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet ',
                        metavar='str',
                        type=str,
                        default='Stranger')
   
    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point ',
                        action='store_true')

    return parser.parse_args()

# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting 
    name = args.name
    ending = args.excited
    
    if args.excited == 1:
        ending = '!'
        
    else:
        ending = '.'
 
    print(greeting+', '+name+ending)
    
# --------------------------------------------------

if __name__ == '__main__':
    main()
