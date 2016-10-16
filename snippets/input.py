#!/usr/bin/env python3

import argparse
import gzip

def main():
    counts = {}
    ld_table = {}
    args = argparsing()
    with gzip.open(args.ldgzip, 'rt') as f:
        getLDs(f, counts, ld_table)

    #Sample output
    for i in range(1, 3):
        list(counts.keys())[i]
        list(ld_table.keys())[i]

def argparsing():

    parser = argparse.ArgumentParser(description='Provide LD gzip with optional required SNPs and blacklisted SNPS')
    parser.add_argument(
        '--ldgzip', required=True, help='Input file generated by PLINK')
    parser.add_argument('--reqSNP', required=False)
    parser.add_argument('--blacklist', required=False)

    args = parser.parse_args()

    return args


def getLDs(inp, counts, ld_table):

    '''Parse lines from input and append to dictionaries'''
    # Check if MAF columns are present.
    index = 5
    for line in inp:
        n = len(line.split())
        if n == 9:
            index = 6
        break;

    # Loop over PLINK output lines.
    for line in inp:
        # Split the line into a list.
        data = line.split()
        # Parse SNP IDs.
        snp1 = data[2]
        snp2 = data[index]
        # Append SNP IDs to dictionary.
        addToDict(snp1, snp2, ld_table)
        addToDict(snp2, snp1, ld_table)
    # Keep count of SNPs in a dictionary.
    for snp in ld_table:
        counts[snp] = len(ld_table[snp])


def addToDict(snp1, snp2, ld_table):
    try:
        ld_table[snp1].add(snp2)
    except:
        ld_table[snp1] = set([snp2])

if __name__ == '__main__':
    main()
