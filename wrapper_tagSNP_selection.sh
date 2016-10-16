#for max_tagSNP in 1000 2000 5000 10000 20000 50000; do

python3 \
 2016_project_9/scaffold.py \
  --in ESN.txt YRI.txt LWK.txt MSL.txt GWD.txt \
  --out chrom20 \
  --min_LD 0.8 \
  --min_MAF 0.02 \
  --max_window 200000 \
  --max_tagSNP 1000 2000 5000 10000 20000 50000 \

#  --preselected data/poollist.chrom20.common.snps \

#done
