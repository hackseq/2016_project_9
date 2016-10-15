#!/usr/bin/env python3
import argparse
import gzip

def argparsing:
    parser = argparse.ArgumentParser(description='Provide LD gzip with optional required SNPs and blacklisted SNPS')
    parser.add_argument('--ldgzip', required=True)
    parser.add_argument('--reqSNP', required=False)
    parser.add_argument('--blacklist', required=False)

    args = parser.parse_args();
    return args

def getLDs(inp,counts, ld_table):
  for line in inp:
    data =line.split()
    snp1 = data[2]
    snp2 = data[6]
    addToDict(snp1, snp2, ld_table)
    addToDict(snp2, snp1, ld_table)
  for snp in ld_table:
      counts[snp] = len(ld_table[snp])

def addToDict(snp1, snp2, ld_table):
    if snp1 in ld_table:
        ld_table[snp1].add(snp2)
    else:
        ld_table[snp1]=set([snp2])

def main():
    counts = {}
    ld_table = {}
    args = argparsing()
    with gzip.open(args.ldgzip, 'rt') as f:
        getLDs (f, counts, ld_table)

