#! /usr/bin/env python3

import sys
import os
import time


def add(snp1,snp2):
    if snp1 in ld_table:
        ld_table[snp1].add(snp2)
    else:
        ld_table[snp1]=set([snp2])

def getLDs(inp,counts):
  for line in inp:
    data =line.split()
    snp1 = data[2]
    snp2 = data[6]
    add(snp1,snp2)
    add(snp2,snp1)
  for snp in ld_table:
      counts[snp] = len(ld_table[snp])


ld_table = {}
counts = {}

inp = open(sys.argv[1])
getLDs(inp,counts)

    
