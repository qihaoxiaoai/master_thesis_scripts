#utf-8
#qihaoxiaoai@gmail.com
import os
import sys
import subprocess
import numpy as np
import glob
def make_plumed_input(num_bp, strand):
    atom_pairs = []
    if strand == "d":
        s1 = [i*3 + 1 for i in range(num_bp)]
        s2 = [i*3 + num_bp*3 for i in range(num_bp)]
        for idx, (b1, b2) in enumerate(zip(s1, reversed(s2))):
            atom_pairs.append((b1, b2))
    else:
        print("not developed yet!")
    pairlist= '#pair_distance \n'
    paird = 'd1: DISTANCES'
    plumed_out ='PRINT ARG='
   
    # add each pair with plumed ormat
    for i, pair in enumerate(atom_pairs):
        pairlist +=f'p{i+1}: DISTANCE ATOMS={pair[0]},{pair[1]} \n'
        paird += f' ATOMS{i+1}={pair[0]},{pair[1]}'
        plumed_out += f'p{i+1},'
    paird += ' MEAN\n'
    plumed_out +='d1.mean,metad.bias STRIDE=5000 FILE=COLVAR \n'
    plumed_para ='METAD ...\nLABEL=metad\nARG=d1.mean  # take the mean of all distanes\nPACE=1000\nHEIGHT=0.6 #1.2\nSIGMA=0.01 #0.35\nFILE=HILLS\nBIASFACTOR=4\nTEMP=315.0\nGRID_MIN=0.45\nGRID_MAX=7.5\n... METAD\n'
    return pairlist,paird,plumed_out,plumed_para

input_bp=int(sys.argv[1])
atom_pairs = make_plumed_input(input_bp,"d")
with open(f'plumed.dat', 'w') as f:
    f.write(atom_pairs[0])
    f.write(atom_pairs[1])
    f.write(atom_pairs[3])
    f.write(atom_pairs[2])
    f.close()

