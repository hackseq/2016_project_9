#!/usr/bin/env python3

import argparse
import os
import subprocess

#output a shell script to run plink on the files we split by chromosome and population
def main():
    args = argparsing()
    
    #take population names from input file 
    with open(args.popnames, 'r') as myfile:
        pop_names=myfile.read().split()
    print(pop_names)
    print(type(pop_names))
    
    #populate vectors with optional arguments
    if args.maf:
        maf = "--with-freqs"
    else:
        maf=""
    
    for pop_name in pop_names:
        run_plink = "for i in {1.." \
        + args.chrnum \
        + "}; do " \
        + args.plink_path \
        + "plink --vcf " \
        + pop_name \
        + ".vcf " \
        + "--r2 " \
        + maf \
        + " --out " \
        + pop_name \
        + "_chr${i}" \
        + "; done" 
        #subprocess.run(run_plink, shell = True)
        print(run_plink)

def argparsing():
    parser = argparse.ArgumentParser(description='wrapper for plink commands')
    parser.add_argument('--vcf', required=True, help='Input VCF files split by chromosome and population')
    parser.add_argument('--chrnum', required=True, help='number of chromosome files')
    parser.add_argument('--popnames', required=True, help='file with pop names')
    parser.add_argument('--plink_path', required=True, help='path to plink')
    parser.add_argument('--maf', required=False, help='return MAF values')
    #parser.add_argument('--', required=False, help='')

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    main()
