#!/usr/bin/env python3

import sys
import pysam

def main():
    d_args = {'out': sys.stdout,
              'ref': '/home/tcarstensen/data/hs37d5.fa.gz'
             }
    setT = set()
    for line in sys.stdin:
        setT.add(line)
    write_output_vcf(d_args, setT)

def write_output_vcf(d_args, setT):
    reference_fasta = pysam.Fastafile(d_args['ref'])
    with d_args['out'] as f:
        # VCF Header
        f.write('##fileformat=VCFv4.2\n')
        f.write('##reference=' + d_args['ref'] + '\n')

        # 8 mandatory columns for VCF file
        f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")

        for snp in setT:
            (chrom, pos) = snp.rstrip().split(':')
            ident = '.'
            start = int(pos) - 1
            end = int(pos)
            ref = reference_fasta.fetch(chrom, start, end)
            alt = '.'
            qual = '.'
            filt = '.'
            info = '.'
            f.write('\t'.join([chrom, pos, ident, ref, alt, qual, filt, info]) + '\n')
        
if __name__ == '__main__':
    main()
