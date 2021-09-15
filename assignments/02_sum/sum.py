#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-09-14
Purpose: Rock the Casbah
"""
import argparse

# --------------------------------------------------

def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description ='Add numbers',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar = 'INT',
                        type = int,
                        nargs = '+',
                        help = 'Numbers to add')

    return parser.parse_args()

# --------------------------------------------------

def find_sum(num_digits, nums):
    """ Find the total sum of the numbers entered """

    sum = 0

    for count in range (num_digits):
            sum = sum + nums[count]

    return sum

# --------------------------------------------------

def print_function(num_digits, nums, total_sum):
    """ Print out the numbers being added along with the answer """

    for count in range (num_digits):

        if count == num_digits - 1:
            print (nums[count], end = '')
            print (" = ", end = '')
            print (total_sum)

        else:    
            print (nums[count], end = '')
            print (' + ', end = '')

# --------------------------------------------------

def main():
    """ Make a jazz noise here """

    args = get_args()
    nums = args.numbers
    num_digits = len (nums)
    total_sum = find_sum(num_digits, nums)

    print_function(num_digits, nums, total_sum)

# --------------------------------------------------

if __name__ == '__main__':
    main()
