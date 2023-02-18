#!/usr/bin/env python

# Import packages and functions required
import sys, re
from argparse import ArgumentParser

# Defines the arguments that will be received as input
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# If the length of the input sequence is 1, exits the script
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Identifies whether the sequence is DNA or RNA
# The 'if not' is added to avoid classifying a sequence that contains T and U as DNA or RNA
args = parser.parse_args()
args.seq = args.seq.upper() # Transforms the sequence in upper case
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        if not re.search('U', args.seq):
            print ('The sequence is DNA')
        else:
            print ('Please check the sequence, it contains both T and U')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Identifies whether the sequence contains a motif specified
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("The motif was found, that's great!")
    else:
        print("The motif was not found")
