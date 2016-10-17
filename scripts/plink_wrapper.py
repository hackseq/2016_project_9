#!/usr/bin/env python3

### Possible improvements ###
### Replace for loops with something faster
### Have the plink commands run in parallel somehow
### popnames and plinkpanel are slightly redundant
### 
###

import argparse
import os
import subprocess

#output a shell script to run plink on the files we split by chromosome and population
def main():
    args = argparsing()
    
    #take population names from input file 
    with open(args.popnames, 'r') as myfile:
        set_pops = set([line.rstrip().split()[0] for line in myfile])
    
    #populate vectors with optional arguments
    if args.maf:
        maf = "with-freqs"
    else:
        maf = ""
    if args.chrnum:
        chr = " --chr " + args.chrnum
        numchr=args.chrnum
    else:
        chr = ""
        numchr="2"
        
    #populate and run plink commands
    for vcf in args.vcf:    
        for pop_name in set_pops:
            for i in range(1,int(numchr)):
                run_plink = args.plinkpath \
                + "plink --vcf " \
                + vcf \
                + " --attrib-indiv " \
                + args.plinkpanel \
                + " " \
                + pop_name \
                + chr \
                + " --r2 gz " \
                + maf \
                + " --out " \
                + pop_name \
                + "_chr" \
                + str(i)
                subprocess.run(run_plink, shell = True)

def argparsing():
    parser = argparse.ArgumentParser(description='wrapper for plink commands')
    parser.add_argument('--vcf', nargs='+', required=True, help='Input VCF file name')
    parser.add_argument('--popnames', required=True, help='tab-separated file (popid indid)')
    parser.add_argument('--plinkpath', required=True, help='path to plink')
    parser.add_argument('--plinkpanel', required=True, help='panel of individuals in plink format in your dataset')
    parser.add_argument('--chrnum', required=False, help='number of chromosomes in your vcf file')
    parser.add_argument('--maf', required=False, action="store_true", help='return MAF values')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    main()
