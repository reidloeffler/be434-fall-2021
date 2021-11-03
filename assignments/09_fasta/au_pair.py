#!/usr/bin/env python3
"""
Author : reidloeffler <reidloeffler@localhost>
Date   : 2021-11-02
Purpose: Assignment 9
"""

import argparse
from Bio import SeqIO
import os

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_files',
                        type=str,
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+')

    parser.add_argument('-o',
                        '--outdir',
                        type=str,
                        metavar='str',
                        help='Output directory',
                        default='split')

    return parser.parse_args()


# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    input_files = (args.input_files)
    out_dir = args.outdir
    # Command line arguments

    for file_path in input_files:

        input_file = SeqIO.parse(file_path, 'fasta')
        file_name = os.path.basename(file_path)
        root, ext = os.path.splitext(file_name)
        # Obtains file name, root, and extension from input file

        if os.path.exists(out_dir) is False:
            os.mkdir(out_dir)
        # Checks if output directory exist

        out_file_1 = open(os.path.join(out_dir, root + '_1' + ext), 'w', encoding='UTF-8')
        out_file_2 = open(os.path.join(out_dir, root + '_2' + ext), 'w', encoding='UTF-8')
        # Builds path for each output file

        track = 1
        # Variable used to track input file line

        for line in input_file:

            if track % 2 != 0:
                print('>' + line.id, file=out_file_1)
                print(str(line.seq), file=out_file_1)
            # Prints info from odd lines to the first output file

            else:
                print('>' + line.id, file=out_file_2)
                print(str(line.seq), file=out_file_2)
            # Prints info from even lines to the second output file

            track += 1
            # Tracks input file line

    print(f'Done, see output in "{out_dir}"')
    # Prints the output directory


# --------------------------------------------------
if __name__ == '__main__':
    main()
