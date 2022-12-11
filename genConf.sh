#!/bin/bash
export X3DNA=/home/xhshi/hjx/software-self/lammps-simple/x3dna/x3dna-v2.4
export PATH=/home/xhshi/hjx/software-self/lammps-simple/x3dna/x3dna-v2.4/bin:$PATH
export LD_LIBRARY_PATH=/home/xhshi/hjx/software-self/lammps-simple/x3dna/x3dna-v2.4/lib:$LD_LIBRARY_PATH

spn2cdir="/home/xhshi/hjx/software-self/lammps-simple/USER-3SPN2" # setup 3SPN path

${spn2cdir}/DSIM_ICNF/icnf.exe seq 0 1 . 0 # conf_lammps.in, in00_conf.xyz, in00_cvmd.psf 
