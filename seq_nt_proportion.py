#!/usr/bin/env python

# Script to calculate the proportion of nucleotides in a DNA or RNA sequence

# Import packages and functions required
import sys, re
from argparse import ArgumentParser

# Defines the arguments that will be received as input
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# If the length of the input sequence is 1, exits the script
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)


# Defines the arguments that will be received as input
parser = ArgumentParser(description = 'Calculate the proportion of nucleotides in a sequence')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# Calculates the proportion of nucleotides
args = parser.parse_args()
args.seq = args.seq.upper() # Transforms the sequence in upper case

# Counter of each nucleotide to 0
A_count = 0
C_count = 0
G_count = 0
T_count = 0
U_count = 0

for nt in args.seq:
    if nt == 'A' :
        A_count = A_count + 1
    elif nt == 'C' :
        C_count = C_count + 1
    elif nt == 'G' :
        G_count = G_count + 1
    elif nt == 'T' :
        T_count = T_count + 1
    elif nt == 'U' :
        U_count = U_count + 1

length = len(args.seq)

print ("The proportion of nucleotides in the sequence is as follows for A, C, G, T and U: ", 
(float(A_count)/length)*100,(float(C_count)/length)*100,(float(G_count)/length)*100,(float(A_count)/length)*100,(float(T_count)/length)*100,(float(U_count)/length)*100)


