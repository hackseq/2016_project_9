#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Provide VCF with optional required SNPs and blacklisted SNPS')
parser.add_argument('--vcf', required=True)
parser.add_argument('--reqSNP', required=False)
parser.add_argument('--blacklist', required=False)

args = parser.parse_args();
