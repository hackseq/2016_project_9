#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Given a three-letter population ID and a .ped file,";
    echo "Return a list of individual ids (one per line)";
    echo "";
    echo "Usage: $0 [population_id] [ped_file]";
    echo "";
    echo "example: $0 YRI integrated_call_samples_v2.20130502.ALL.ped";
    exit 1;
fi

POPULATION=$1
PEDFILE=$2

awk -v pop=$POPULATION 'BEGIN{ORS=","} $7==pop{print $2}' < $PEDFILE | tr ',' '\n'
