#!/usr/bin/env python3

import sys
# import vcf

def main():
    d_args = {'out': sys.stdout}
    setT = set()
    for line in sys.stdin:
        setT.add(line)
    write_output_vcf(d_args, setT)

def write_output(d_args, setT, d_setQ):

    with open('{}.tagSNPs'.format(d_args['out']), 'w') as f:
        for ID in setT:
            f.write('{}\n'.format(ID))
    with open('{}.tagged'.format(d_args['out']), 'w') as f:
        for i_pop, setQ in d_setQ.items():
            for ID in setQ:
                f.write('{}:{}\n'.format(i_pop,ID))

    return

def write_output_vcf(d_args, setT):
    # These objects might be used to create full valid VCF file, not used yet.
    # vcf_reader = vcf.Reader(d_args['in'][0], 'r')
    # vcf_writer = vcf.Writer(d_args['out'], vcf_reader)

    with d_args['out'] as f:
        # 8 mandatory columns for VCF file
        f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
        # To start with, just print Chrom & Pos
        for snp in setT:
            f.write(snp.rstrip().replace(':','\t') + '\t.\t.\t.\t.\t.\t.\n')
        
if __name__ == '__main__':
    main()
