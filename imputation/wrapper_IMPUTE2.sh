#!/bin/bash

chrom=20

Ne=17469
k_hap=500
k=80
iter=30

impute2=bin/impute2

for pop in LWK ESN MSL YRI GWD; do

h=data/imputation/1000GP_Phase3_minus_$pop/1000GP_Phase3_chr$chrom.hap.gz
l=data/imputation/1000GP_Phase3_minus_$pop/1000GP_Phase3_chr$chrom.legend.gz
m=data/imputation/genetic_map_chr${chrom}_combined_b37.txt


out=out_IMPUTE/$pop.$chrom
mkdir -p $(dirname $out)
if [ -f $out.touch ]; then continue; fi
touch $out.touch

$impute2 \
 -m $m \
 -h $h \
 -l $l \
 -Ne $Ne \
 -known_haps_g data/imputation/$pop.hap.gz \
 -o $out \
 -k_hap $k_hap \
 -k $k \
 -iter $iter \
 -allow_large_regions \
 -int 1 63000000 \

done
