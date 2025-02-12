#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import math
import time

def printHeader():
    print(" Required inputs:")
    print("   1. Molecular QMeCha *.xyz file")
    print(" Optional inputs:")
    print("   2. The number of integration points (integer) [Default 8]")
    print("   3. The energy cut off (float) [Default = 0.0001]")
    print("   4. Pseudo integration method LA or DLA (string) [Default = 'DLA']")

def printPseudoFile():
    psdOutFileName = 'pseudo.dat'
    psdOutFile = open(psdOutFileName, "w" )
    psdOutFile.write("&pseudo\n")
    psdOutFile.write("n_pseudo       ="+str(n_pseudo)+'\n')
    psdOutFile.write("n_psd_grd_pnts ="+str(n_psd_grd_pnts)+'\n')
    psdOutFile.write("ene_psd_cut    ="+str(ene_psd_cut)+'\n')
    psdOutFile.write("psd_int_mthd   ="+str(psd_int_mthd)+'\n')
    psdOutFile.write("/\n")
    for i in atom_names :
        print_ccECP_pseudo(i,psdOutFile)
    psdOutFile.close()

def print_ccECP_pseudo(atom,outFile):
    psdFile =open(qmecha_dir+'/pseudopotentials/ccECP/'+atom+'.ccECP.qmecha', 'r')
    psdFileLines=psdFile.readlines()
    for line in range(len(psdFileLines)) :
        outFile.write(str(psdFileLines[line]))
    psdFile.close()


print(" =======================================================================")
print(" ===================== Pseudo generator for QMeCha =====================")
print(" =======================================================================")
try:
    qmecha_dir=os.environ['QMECHA_DIR']
except:
    print(" $QMECHA_DIR environment variable not set")
    print(" run:")
    print("  setenv QMECHA_DIR=../QMeCha_dev")
    print(" or")
    print("  export QMECHA_DIR=../QMeCha_dev")
    exit()

try:
    molFileName = sys.argv[1]
    molFile = open(molFileName, "r" )
    molFileLines = molFile.readlines()
    atom_names = []
    for line_num in range(len(molFileLines)) :
        if ("n_at" in molFileLines[line_num]) :
            try:
                n_at = int(molFileLines[line_num].split()[2])
            except:
                n_at = 0
        if ("/" in molFileLines[line_num]) :
            read_from = line_num + 1
            break
    for line_num in range(read_from,read_from+n_at) :
        atom_names.append(molFileLines[line_num].split()[0])
    atom_names = list( dict.fromkeys(atom_names) )
    #Remove non pseudo atoms.
    atom_names =[ atom for atom in atom_names if '*' in atom ]

    for line_num in range(len(atom_names)) :
        atom_names[line_num]=atom_names[line_num].replace('*', '')

    n_pseudo = len(atom_names)
except:
    print(" Couldn't open file molecular QMeCha file")
    printHeader()
    exit()

try:
    n_psd_grd_pnts = int(sys.argv[2])
except:
    print(" Number of intergration points not specified setting to Default [n_psd_grd_pnts = 8]")
    n_psd_grd_pnts = 8

try:
    ene_psd_cut    = float(sys.argv[3])
except:
    print(" Energy cut-off not specified setting to Default [ene_psd_cut = 0.0001]")
    ene_psd_cut    = 0.0001

try:
    if ( str(sys.argv[4])=='LA' ) :
        psd_int_mthd   = 0
    else :
        psd_int_mthd   = 1
except:
    print(" Pseudo integration method not specified setting to Default [psd_int_mthd = 1 (DLA)]")
    psd_int_mthd   = 1

printPseudoFile()


