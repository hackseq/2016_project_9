#!/usr/bin/env python3

import sys
import vcf

def main():
    d_args = {'out': sys.stdout,
              'pretagged': None,
              'min_LD': 0.80,
              'min_MAF': 0.01,
              'in': ['../../data/ALL.chr20.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz'],
              'max_window': 250000,
              'preselected': None,
              'max_tagSNP': 1000000,
    }
    
    setT = set('20:1280','20:256','20:2048','20:65535')
    print(setT)
    d_setQ = {}
    print(d_setQ)
#   write_output(d_args, setT, d_setQ)
    write_output_vcf(d_args, setT, d_setQ)

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
    vcf_reader = vcf.Reader(d_args['in'][0], 'r')
    vcf_writer = vcf.Writer(d_args['out'], vcf_reader)
    
if __name__ == '__main__':
    main()
