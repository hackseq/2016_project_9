#! /usr/bin/env python
"""
"""
from __future__ import print_function
from multiprocessing import Pool, cpu_count
from glob import glob
import argparse
import os.path
import shutil
import gzip
import sys

def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', "--inputfolder", required=True,
        metavar="INPUT_FOLDER", help="path to the input folder")
    parser.add_argument('-t',"--threads", default=cpu_count()-1, type=int,
        metavar="THREADS", help="number of threads")
    parser.add_argument('-o',"--outputfolder", required=True,
        metavar="OUTPUT_FOLDER", help="path to the output folder")
    parser.add_argument( "-p", "--popnames" ,required=True,
        help="name of pop(s) to exclude")
    return parser.parse_args()

def multi_run_wrapper(args):
    """enables multiprocessing with more than one params
    Keyword arguments:
    args -- a list of tuples, ech in the form (infilename,outfilename,indices)
    """
    return filter_haps_file(*args)

def filter_haps_file(infilename, outfilename, indices):
    """ makes a new haps.gz file, keeping only the samples in an index list
    Keyword arguments:
    infilename -- input gz file
    outfilename -- output hap.gz file
    indices -- indices to keep (for i in indices, i*2 and i*2+1 are kept)
    """
    fin = gzip.open(infilename)
    fout = gzip.open(outfilename,"wt")
    #print("filtering file: %s"%outfilename)
    linecount = 0
    for line in fin:
        linecount += 1
        row = line.strip().split()
        newrow = ["%s %s"%(row[i*2],row[i*2+1]) for i in indices]
        newline = " ".join(newrow) + "\n"
        fout.write(newline)
        if linecount % 10000 == 0:
            #print("%s\t%i"%(outfilename,linecount))
            pass
    fout.close()
    fin.close()

def get_sample_indices(samplefilename, newsamplefilename, pops):
    """ given a pop name, writes a new samplefile, and returns indices of samples NOT in those pops
    Keyword arguments:
    samplefilename -- input sample file
    newsamplefilename -- output sample file
    pops -- list of pops to remove
    """
    indices = []
    fin = open(samplefilename)
    fout = open(newsamplefilename,"wt")
    head = fin.readline()
    #print("removing: %s"%str(pops))
    fout.write(head)
    for i,line in enumerate(fin):
        sample, population, superpop, gender = line.strip().split()
        if population not in pops:
            indices.append(i)
            #print("-",end="")
            fout.write(line)
        else:
            pass
            #print("+",end="")
    fin.close()
    fout.close()
    return indices 

def main():
    args = parse_args()
    hapfiles = glob(os.path.join(args.inputfolder, "*.hap.gz"))
    worklist = []
    inputsamplefilename = os.path.join(args.inputfolder,"1000GP_Phase3.sample")
    outputsamplefilename = os.path.join(args.outputfolder,"1000GP_Phase3.sample")
    indices = get_sample_indices(inputsamplefilename, outputsamplefilename, args.popnames)
    for infilename in hapfiles:
        shutil.copy(infilename.replace(".hap.gz",".legend.gz"),args.outputfolder)
        shutil.copy(infilename.replace(".hap.gz","_combined_b37.txt").replace("1000GP_Phase3_","genetic_map_"),args.outputfolder)
        outfilename = os.path.join(args.outputfolder, os.path.basename(infilename))
        worklist.append((infilename,outfilename,indices))
    pool = Pool(args.threads)
    results = pool.map(multi_run_wrapper,worklist)

if __name__ == "__main__":
    main()
