            #!/usr/bin/env python

import subprocess

pop_names=["Eur","Afr","Asn"] #take population name from somewhere upstream

#output a shell script to run plink on the files we split by chromosome and population
for pop_name in pop_names:
    run_plink = "for i in {1..24}; do " \
    + "plink --vcf " \
    + pop_name \
    + "_chr${i}.vcf" \
    + " --r2" \
    + " --with-freqs" \
    + " --make-bed" \
    + " --out " \
    + pop_name \
    + "_ld_maf" \
    + "; done" 
    subprocess.run(run_plink, shell = True)
#run the shell command
subprocess.run(run_plink, shell = True)
