#!/bin/bash
INFOLDER=input/
OUTPUTROOT=output

set -e 

for POPNAME in XXX ESN GWD LWK MSL YRI
do
OUTFOLDER=${OUTPUTROOT}/1000GP_Phase3_minus_${POPNAME}
mkdir -p ${OUTFOLDER}
python ./make_impute2_refset.py -t 24 -p ${POPNAME} -i ${INFOLDER} -o ${OUTFOLDER} &
done
exit
