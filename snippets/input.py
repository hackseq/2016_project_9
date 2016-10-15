#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Provide VCF with optional required SNPs and blacklisted SNPS')
parser.add_argument('--vcf', required=True)
parser.add_argument('--reqSNP', required=False, help='Text file with pre-selected SNPs with one SNP ID per line')
parser.add_argument('--blacklist', required=False, help='SNPs not to include in the set of candidate SNPs')

args = parser.parse_args();
