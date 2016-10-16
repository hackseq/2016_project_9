# HackSeq 2016: Project 9
## Selection of tag SNPs for an African SNP array by LD and haplotype based methods

### Summary
Project 9 aims to develop a memory efficient tool for SNP selection from whole genome sequence (WGS) data. Users may provide commercial lists of pre-aproved SNPs, lists of SNPs of general interest, and list of SNPs to exclude. 

### Algorithm
The algorithm selects SNPs that tag other SNPs most efficient across individuals from several African populations. It is based on haplotype (multi-marker) tagging in addition to simple pairwise LD. By using random access to block gzipped files, the algorithm can efficiently process WGS data. 

### Get the tool
[Link]

### Language
Python 3.x

### Dependencies
[PLINK](https://www.cog-genomics.org/plink2)
[pysam](https://pysam.readthedocs.io/en/latest/index.html)

### See more 
[Wiki](https://github.com/hackseq/2016_project_9/wiki)
