#!/bin/bash
#INFOLDER=test_input/
INFOLDER=input
OUTPUTROOT=output

set -e 

for POPNAME in NONE ESN GWD LWK MSL YRI
#for POPNAME in NONE ESN
do
OUTFOLDER=${OUTPUTROOT}/1000GP_Phase3_minus_${POPNAME}
mkdir -p ${OUTFOLDER}
python ./make_impute2_refset.py -t 24 -p ${POPNAME} -i ${INFOLDER} -o ${OUTFOLDER}
done
exit
