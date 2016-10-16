#!/usr/bin/env python3

import argparse
import os
import subprocess

#output a shell script to run plink on the files we split by chromosome and population
def main():
    args = argparsing()
    
    #take population names from input file 
    with open(args.popnames, 'r') as myfile:
        set_pops = set([line.rstrip().split()[0] for line in myfile])
    print(set_pops) #remove later
    
    #populate vectors with optional arguments
    if args.maf:
        maf = "with-freqs"
    else:
        maf = ""
    if args.chrnum:
        chr = " --chr " + args.chrnum
        numchr=args.chrnum #maybe unnecessary 
    else:
        chr = ""
        numchr="1"
        
    #populate and run plink commands
    for vcf in args.vcf:    
        for pop_name in set_pops:
            for i in range(1,int(numchr)):
                run_plink = args.plinkpath \
                + "plink --vcf " \
                + vcf \
                + " --attrib-indiv " \
                + args.popnames \
                + " " \
                + pop_name \
                + chr \
                + " --r2 gz " \
                + maf \
                + " --out " \
                + pop_name \
                + "_chr" \
                + str(i)
                print(run_plink) #remove later
                subprocess.run(run_plink, shell = True)

def argparsing():
    parser = argparse.ArgumentParser(description='wrapper for plink commands')
    parser.add_argument('--vcf', nargs='+', required=True, help='Input VCF file name')
    parser.add_argument('--popnames', required=True, help='tab-separated file in plink keep format (popid indid)')
    parser.add_argument('--plinkpath', required=True, help='path to plink')
    parser.add_argument('--chrnum', required=False, help='number of chromosomes in your vcf file')
    parser.add_argument('--maf', required=False, action="store_true", help='return MAF values')
    #parser.add_argument('--', required=False, help='')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    main()
